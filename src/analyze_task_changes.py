
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Locate project folder
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Read the comparison file created in the previous step
file_path = (
    PROJECT_DIR
    / "outputs"
    / "april_may_task_comparison.csv"
)

df = pd.read_csv(file_path)

# Calculate absolute change (size of change, ignoring direction)
df["absolute_change"] = df["change_pp"].abs()

print("APRIL–MAY 2026 TASK USAGE ANALYSIS")
print("----------------------------------")

print("Total matched tasks:", len(df))

print("\nSUMMARY STATISTICS")
print("Average change:", round(df["change_pp"].mean(), 4))
print("Median change:", round(df["change_pp"].median(), 4))
print("Average absolute change:", round(df["absolute_change"].mean(), 4))
print("Largest increase:", round(df["change_pp"].max(), 4))
print("Largest decrease:", round(df["change_pp"].min(), 4))

print("\nSIZE OF CHANGES")
print("No recorded change:", (df["absolute_change"] < 0.000001).sum())
print("Change >= 0.01 pp:", (df["absolute_change"] >= 0.01 - 1e-9).sum())
print("Change >= 0.05 pp:", (df["absolute_change"] >= 0.05 - 1e-9).sum())
print("Change >= 0.10 pp:", (df["absolute_change"] >= 0.10 - 1e-9).sum())

# Create folder for charts
figures_dir = PROJECT_DIR / "figures"
figures_dir.mkdir(exist_ok=True)

# Histogram of percentage-point changes
plt.figure(figsize=(10, 5))
plt.hist(df["change_pp"], bins=40, edgecolor="black")
plt.xlabel("Change in task usage (percentage points)")
plt.ylabel("Number of tasks")
plt.title("Distribution of Claude Task Usage Changes: April–May 2026")
plt.tight_layout()

chart_path = figures_dir / "april_may_change_distribution.png"
plt.savefig(chart_path, dpi=300)
plt.close()

print("\nChart saved to:", chart_path)
