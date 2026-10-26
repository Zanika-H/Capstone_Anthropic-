
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]

# Earlier comparison
earlier = pd.read_csv(
    PROJECT_DIR / "outputs"
    / "earlier_release_task_comparison.csv"
)

# June release
june = pd.read_csv(
    PROJECT_DIR / "data"
    / "release_2026_06_26"
    / "aei_claude_ai_2026-06-26.csv",
    low_memory=False
)

# Keep global, individual O*NET task percentages
june_tasks = june[
    (june["category_name"] == "onet")
    & (june["metric_id"] == "pct")
    & (june["hierarchy_level"] == 0)
    & (june["geo_id"] == "GLOBAL")
].copy()

# Standardize June task names
june_tasks["task_key"] = (
    june_tasks["node_name"]
    .astype("string")
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", " ", regex=True)
)

# Separate April and May
april = june_tasks[
    june_tasks["date_start"] == "2026-04-01"
].copy()

may = june_tasks[
    june_tasks["date_start"] == "2026-05-01"
].copy()

# Earlier tasks found in all three periods
earlier_tasks = set(
    earlier["task_key"].dropna()
) - {"none"}

april_tasks = set(april["task_key"].dropna())
may_tasks = set(may["task_key"].dropna())

# Tasks present in all five collection periods
shared_tasks = (
    earlier_tasks
    & april_tasks
    & may_tasks
)

print("LONGITUDINAL TASK OVERLAP")
print("-------------------------")
print("Earlier matched classified tasks:", len(earlier_tasks))
print("April 2026 unique task names:", len(april_tasks))
print("May 2026 unique task names:", len(may_tasks))

print("\nEarlier tasks also found in April:",
      len(earlier_tasks & april_tasks))

print("Earlier tasks also found in May:",
      len(earlier_tasks & may_tasks))

print("\nTASKS SHARED ACROSS ALL FIVE PERIODS:",
      len(shared_tasks))

# Save shared task names
output_dir = PROJECT_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

output_path = output_dir / "five_period_shared_tasks.csv"

pd.DataFrame({
    "task_key": sorted(shared_tasks)
}).to_csv(output_path, index=False)

print("\nSaved:", output_path)
