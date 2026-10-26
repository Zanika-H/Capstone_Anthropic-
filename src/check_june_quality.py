
from pathlib import Path
import pandas as pd

# Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Locate the June 2026 dataset
file_path = (
    PROJECT_DIR
    / "data"
    / "release_2026_06_26"
    / "aei_claude_ai_2026-06-26.csv"
)

# Load the data
df = pd.read_csv(file_path, low_memory=False)

# Keep only global individual O*NET tasks
tasks = df[
    (df["category_name"] == "onet")
    & (df["metric_id"] == "pct")
    & (df["hierarchy_level"] == 0)
    & (df["geo_id"] == "GLOBAL")
].copy()

# Convert percentages to numbers
tasks["value"] = pd.to_numeric(tasks["value"], errors="coerce")

print("JUNE 2026 DATA QUALITY CHECK")
print("----------------------------")

# Check duplicate task IDs within the same month
duplicates = tasks.duplicated(
    subset=["date_start", "node_external_id"]
).sum()

print("Duplicate month/task ID combinations:", duplicates)

# Check missing data
print("Missing task IDs:", tasks["node_external_id"].isna().sum())
print("Missing percentages:", tasks["value"].isna().sum())

# Check percentage values
print("Minimum percentage:", tasks["value"].min())
print("Maximum percentage:", tasks["value"].max())

# Check each month separately
print("\nRESULTS BY MONTH")

for month, group in tasks.groupby("date_start"):
    print(f"\nMonth: {month}")
    print("Rows:", len(group))
    print("Unique task IDs:", group["node_external_id"].nunique())
    print("Missing percentages:", group["value"].isna().sum())
    print(
        "Duplicate task IDs:",
        group.duplicated(subset=["node_external_id"]).sum()
    )
