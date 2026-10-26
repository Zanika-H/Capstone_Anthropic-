
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parents[1]

file_path = (
    PROJECT_DIR
    / "outputs"
    / "earlier_release_task_comparison.csv"
)

df = pd.read_csv(file_path)

# Remove unclassified placeholder task
df = df[
    df["task_key"].str.strip().str.lower() != "none"
].copy()

print("CROSS-RELEASE CHANGE ANALYSIS")
print("-----------------------------")
print("Matched classified tasks:", len(df))

periods = {
    "August to November": "aug_to_nov_pp",
    "November to February": "nov_to_feb_pp",
    "August to February": "aug_to_feb_pp"
}

for label, column in periods.items():
    changes = df[column]
    absolute = changes.abs()

    print(f"\n{label}")
    print("Average change:", round(changes.mean(), 4))
    print("Median change:", round(changes.median(), 4))
    print("Average absolute change:", round(absolute.mean(), 4))
    print("Change >= 0.05 pp:", (absolute >= 0.05).sum())
    print("Change >= 0.10 pp:", (absolute >= 0.10).sum())
    print("Change >= 0.50 pp:", (absolute >= 0.50).sum())

# Visualize August to February changes
figures_dir = PROJECT_DIR / "figures"
figures_dir.mkdir(exist_ok=True)

plt.figure(figsize=(10, 5))
plt.hist(df["aug_to_feb_pp"], bins=50, edgecolor="black")
plt.xlabel("Change in task usage (percentage points)")
plt.ylabel("Number of tasks")
plt.title("Claude Task Usage Changes: August 2025 to February 2026")
plt.tight_layout()

chart_path = figures_dir / "aug_to_feb_change_distribution.png"
plt.savefig(chart_path, dpi=300)
plt.close()

print("\nChart saved:", chart_path)
