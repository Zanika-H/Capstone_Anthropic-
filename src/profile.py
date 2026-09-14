from pathlib import Path
import pandas as pd


# --------------------------------------------------
# Set project and data locations
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


# --------------------------------------------------
# Load the raw Claude.ai dataset
# --------------------------------------------------

claude_file = DATA_DIR / "aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv"

claude_df = pd.read_csv(claude_file)


# --------------------------------------------------
# Basic dataset information
# --------------------------------------------------

print("=" * 60)
print("CLAUDE.AI DATASET PROFILE")
print("=" * 60)

print(f"\nRows: {len(claude_df):,}")
print(f"Columns: {len(claude_df.columns)}")

print("\nColumns:")
print(claude_df.columns.tolist())


# --------------------------------------------------
# Geographic coverage
# --------------------------------------------------

print("\n" + "=" * 60)
print("GEOGRAPHIC COVERAGE")
print("=" * 60)

print(
    claude_df["geography"]
    .value_counts(dropna=False)
)


# --------------------------------------------------
# Facets
# --------------------------------------------------

print("\n" + "=" * 60)
print("FACETS")
print("=" * 60)

print(
    claude_df["facet"]
    .value_counts(dropna=False)
)


# --------------------------------------------------
# Variables
# --------------------------------------------------

print("\n" + "=" * 60)
print("VARIABLES")
print("=" * 60)

print(
    claude_df["variable"]
    .value_counts(dropna=False)
)


# --------------------------------------------------
# Missing values
# --------------------------------------------------

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing = claude_df.isna().sum()

print(missing)


# --------------------------------------------------
# Plot 1: Geographic coverage
# --------------------------------------------------

import matplotlib.pyplot as plt

geography_counts = claude_df["geography"].value_counts()

plt.figure(figsize=(8, 5))
geography_counts.plot(kind="bar")

plt.title("Claude.ai Dataset Records by Geographic Level")
plt.xlabel("Geographic Level")
plt.ylabel("Number of Records")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("geography_coverage.png", dpi=300)
plt.show()

# --------------------------------------------------
# Plot 2: Records by facet
# --------------------------------------------------

facet_counts = claude_df["facet"].value_counts()

plt.figure(figsize=(10, 6))
facet_counts.plot(kind="bar")

plt.title("Claude.ai Dataset Records by Facet")
plt.xlabel("Facet")
plt.ylabel("Number of Records")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("facet_distribution.png", dpi=300)
plt.show()

# --------------------------------------------------
# Plot 3: Records by variable
# --------------------------------------------------

variable_counts = claude_df["variable"].value_counts()

plt.figure(figsize=(10, 6))
variable_counts.plot(kind="bar")

plt.title("Claude.ai Dataset Records by Variable")
plt.xlabel("Variable")
plt.ylabel("Number of Records")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("variable_distribution.png", dpi=300)
plt.show()

#Deeper analysis
# ---------------------------------------------------------
# Consumer vs. Business Task Comparison
# ---------------------------------------------------------

claude_file = DATA_DIR / "aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv"
api_file = DATA_DIR / "aei_raw_1p_api_2025-08-04_to_2025-08-11.csv"

claude = pd.read_csv(claude_file)
api = pd.read_csv(api_file)

# Keep global O*NET task percentages
claude_tasks = claude[
    (claude["geography"] == "global") &
    (claude["variable"] == "onet_task_pct") &
    (~claude["cluster_name"].isin(["none", "not_classified"]))
][["cluster_name", "value"]].rename(
    columns={"value": "claude_pct"}
)

api_tasks = api[
    (api["geography"] == "global") &
    (api["variable"] == "onet_task_pct") &
    (~api["cluster_name"].isin(["none", "not_classified"]))
][["cluster_name", "value"]].rename(
    columns={"value": "api_pct"}
)

# Compare tasks appearing in both datasets
task_comparison = claude_tasks.merge(
    api_tasks,
    on="cluster_name",
    how="inner"
)

task_comparison["difference"] = (
    task_comparison["claude_pct"] -
    task_comparison["api_pct"]
)

print("\nConsumer vs. Business Task Comparison")
print("-" * 50)
print(f"Shared tasks compared: {len(task_comparison)}")

print("\nTop 10 tasks higher in Claude.ai:")
print(
    task_comparison
    .sort_values("difference", ascending=False)
    .head(10)
    .to_string(index=False)
)

print("\nTop 10 tasks higher in 1P API:")
print(
    task_comparison
    .sort_values("difference")
    .head(10)
    .to_string(index=False)
)

# Save results
task_comparison.to_csv(
    PROJECT_ROOT / "task_comparison.csv",
    index=False
)

# ---------------------------------------------------------
# Plot: Largest Consumer vs. Business Task Differences
# ---------------------------------------------------------

top_claude = (
    task_comparison
    .sort_values("difference", ascending=False)
    .head(10)
    .copy()
)

top_api = (
    task_comparison
    .sort_values("difference")
    .head(10)
    .copy()
)

plot_data = pd.concat([top_claude, top_api])

# Shorten task names so the chart is readable
plot_data["short_task"] = plot_data["cluster_name"].str.slice(0, 70)

plt.figure(figsize=(12, 10))

plt.barh(
    plot_data["short_task"],
    plot_data["difference"]
)

plt.axvline(0)

plt.xlabel("Difference in task usage percentage points")
plt.ylabel("O*NET task")
plt.title("Tasks Used Differently in Claude.ai vs. 1P API")

plt.tight_layout()

plt.savefig(
    PROJECT_ROOT / "task_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()