
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]

files = {
    "aug_2025": (
        "release_2025_09_15",
        "aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv"
    ),
    "nov_2025": (
        "release_2026_01_15",
        "aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv"
    ),
    "feb_2026": (
        "release_2026_03_24",
        "aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv"
    )
}

tables = []

for period, (folder, filename) in files.items():
    path = PROJECT_DIR / "data" / folder / filename
    df = pd.read_csv(path, low_memory=False)

    # Keep global task percentage records
    tasks = df[
        (df["facet"] == "onet_task")
        & (df["variable"] == "onet_task_pct")
        & (df["geo_id"] == "GLOBAL")
    ].copy()

    # Standardize task names for matching
    tasks["task_key"] = (
        tasks["cluster_name"]
        .astype("string")
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", " ", regex=True)
    )

    tasks["value"] = pd.to_numeric(
        tasks["value"], errors="coerce"
    )

    # Check data quality before merging
    print(f"\n{period}")
    print("Rows:", len(tasks))
    print("Missing task names:", tasks["task_key"].isna().sum())
    print("Missing percentages:", tasks["value"].isna().sum())
    print("Duplicate standardized task names:",
          tasks["task_key"].duplicated().sum())

    if (
        tasks["task_key"].isna().any()
        or tasks["value"].isna().any()
        or tasks["task_key"].duplicated().any()
    ):
        raise ValueError(
            f"Check missing values or duplicates in {period}"
        )

    # Keep only the columns needed
    tasks = tasks[["task_key", "value"]].rename(
        columns={"value": period + "_pct"}
    )

    tables.append(tasks)

# Match tasks found in ALL three periods
comparison = tables[0]

for table in tables[1:]:
    comparison = comparison.merge(
        table,
        on="task_key",
        how="inner",
        validate="one_to_one"
    )

# Calculate percentage-point changes
comparison["aug_to_nov_pp"] = (
    comparison["nov_2025_pct"]
    - comparison["aug_2025_pct"]
)

comparison["nov_to_feb_pp"] = (
    comparison["feb_2026_pct"]
    - comparison["nov_2025_pct"]
)

comparison["aug_to_feb_pp"] = (
    comparison["feb_2026_pct"]
    - comparison["aug_2025_pct"]
)

print("\nCROSS-RELEASE COMPARISON")
print("------------------------")
print("Tasks matched across all three periods:", len(comparison))

for column in [
    "aug_to_nov_pp",
    "nov_to_feb_pp",
    "aug_to_feb_pp"
]:
    print(f"\n{column}")
    print("Increased:", (comparison[column] > 0).sum())
    print("Decreased:", (comparison[column] < 0).sum())
    print("No recorded change:", (comparison[column] == 0).sum())
    print("Average change:", round(comparison[column].mean(), 4))
    print("Median change:", round(comparison[column].median(), 4))

print("\nTOP 5 AUGUST 2025 TO FEBRUARY 2026 INCREASES")
print(
    comparison.nlargest(5, "aug_to_feb_pp")[
        ["task_key", "aug_2025_pct", "feb_2026_pct", "aug_to_feb_pp"]
    ].to_string(index=False)
)

print("\nTOP 5 AUGUST 2025 TO FEBRUARY 2026 DECREASES")
print(
    comparison.nsmallest(5, "aug_to_feb_pp")[
        ["task_key", "aug_2025_pct", "feb_2026_pct", "aug_to_feb_pp"]
    ].to_string(index=False)
)

# Save results
output_dir = PROJECT_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

output_path = output_dir / "earlier_release_task_comparison.csv"
comparison.to_csv(output_path, index=False)

print("\nSaved:", output_path)
