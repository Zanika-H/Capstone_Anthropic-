
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]

file_path = (
    PROJECT_DIR
    / "data"
    / "release_2026_06_26"
    / "aei_claude_ai_2026-06-26.csv"
)

df = pd.read_csv(file_path, low_memory=False)

# Select global, individual O*NET tasks
tasks = df[
    (df["category_name"] == "onet")
    & (df["metric_id"] == "pct")
    & (df["hierarchy_level"] == 0)
    & (df["geo_id"] == "GLOBAL")
].copy()

tasks["value"] = pd.to_numeric(tasks["value"], errors="coerce")

# Separate April and May
april = tasks[tasks["date_start"] == "2026-04-01"][
    ["node_external_id", "node_name", "value"]
].copy()

may = tasks[tasks["date_start"] == "2026-05-01"][
    ["node_external_id", "node_name", "value"]
].copy()

# Rename percentage columns
april = april.rename(columns={"value": "april_pct"})
may = may.rename(columns={"value": "may_pct"})

# Match the same task IDs between both months
comparison = april.merge(
    may,
    on="node_external_id",
    how="inner",
    suffixes=("_april", "_may"),
    validate="one_to_one"
)

# Calculate percentage-point changes
comparison["change_pp"] = (
    comparison["may_pct"] - comparison["april_pct"]
)

# Show results
print("MATCHED TASKS:", len(comparison))

print("\nTOP 10 INCREASES")
print(
    comparison.nlargest(10, "change_pp")[
        ["node_name_april", "april_pct", "may_pct", "change_pp"]
    ].to_string(index=False)
)

print("\nTOP 10 DECREASES")
print(
    comparison.nsmallest(10, "change_pp")[
        ["node_name_april", "april_pct", "may_pct", "change_pp"]
    ].to_string(index=False)
)

print("\nSUMMARY")
print("Tasks with increases:", (comparison["change_pp"] > 0).sum())
print("Tasks with decreases:", (comparison["change_pp"] < 0).sum())
print("Tasks with no recorded change:", (comparison["change_pp"] == 0).sum())

# Save the comparison
output_dir = PROJECT_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

comparison.to_csv(
    output_dir / "april_may_task_comparison.csv",
    index=False
)

print("\nSaved: outputs/april_may_task_comparison.csv")
