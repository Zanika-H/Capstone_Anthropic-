
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]

# Load earlier three-period comparison
earlier = pd.read_csv(
    PROJECT_DIR / "outputs" /
    "earlier_release_task_comparison.csv"
)

# Load the list of shared tasks
shared = pd.read_csv(
    PROJECT_DIR / "outputs" /
    "five_period_shared_tasks.csv"
)

# Load the June 2026 release
june = pd.read_csv(
    PROJECT_DIR / "data" /
    "release_2026_06_26" /
    "aei_claude_ai_2026-06-26.csv",
    low_memory=False
)

# Keep global individual O*NET task percentages
tasks = june[
    (june["category_name"] == "onet")
    & (june["metric_id"] == "pct")
    & (june["hierarchy_level"] == 0)
    & (june["geo_id"] == "GLOBAL")
].copy()

# Standardize task names
tasks["task_key"] = (
    tasks["node_name"]
    .astype("string")
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", " ", regex=True)
)

tasks["value"] = pd.to_numeric(
    tasks["value"], errors="coerce"
)

# Keep April and May 2026
tasks = tasks[
    tasks["date_start"].isin([
        "2026-04-01",
        "2026-05-01"
    ])
]

# Check for duplicate task names within each month

# Identify task names that are duplicated within a month
duplicate_mask = tasks.duplicated(
    subset=["task_key", "date_start"],
    keep=False
)

ambiguous_names = set(
    tasks.loc[duplicate_mask, "task_key"]
)

print("Ambiguous task names:", len(ambiguous_names))

# Save ambiguous records for documentation
output_dir = PROJECT_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

ambiguous_records = tasks[
    tasks["task_key"].isin(ambiguous_names)
].copy()

ambiguous_records.to_csv(
    output_dir / "ambiguous_june_task_names.csv",
    index=False
)

# Exclude ambiguous names from the name-based comparison
tasks = tasks[
    ~tasks["task_key"].isin(ambiguous_names)
].copy()

print("Remaining June task records:", len(tasks))

# Convert April and May into separate columns
wide = tasks.pivot(
    index="task_key",
    columns="date_start",
    values="value"
).reset_index()

# Rename columns
wide = wide.rename(columns={
    "2026-04-01": "apr_2026_pct",
    "2026-05-01": "may_2026_pct"
})

print("April and May data reshaped successfully!")

# Keep only tasks present in all five periods
longitudinal = shared.merge(
    earlier[
        [
            "task_key",
            "aug_2025_pct",
            "nov_2025_pct",
            "feb_2026_pct"
        ]
    ],
    on="task_key",
    how="inner",
    validate="one_to_one"
)

longitudinal = longitudinal.merge(
    wide[
        ["task_key", "apr_2026_pct", "may_2026_pct"]
    ],
    on="task_key",
    how="inner",
    validate="one_to_one"
)

# Check final dataset
print("FIVE-PERIOD LONGITUDINAL DATASET")
print("--------------------------------")
print("Matched tasks:", len(longitudinal))

print("\nMissing values:")
print(longitudinal.isna().sum())

print("\nFirst five rows:")
print(longitudinal.head().to_string(index=False))

# Save dataset
output_dir = PROJECT_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

output_path = output_dir / "five_period_task_dataset.csv"

longitudinal.to_csv(output_path, index=False)

print("\nSaved:", output_path)
