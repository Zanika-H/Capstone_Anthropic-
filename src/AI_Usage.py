import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------------------------------------
# 1. Load Data
# ---------------------------------------------------------

# Make sure results folder exists
os.makedirs("results", exist_ok=True)

# Load enriched AEI dataset and O*NET metadata
aei = pd.read_csv("data/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv")   # <-- corrected filename
task_meta = pd.read_csv("data/onet_task_statements.csv")

# ---------------------------------------------------------
# 2. Filter to O*NET tasks + automation/augmentation metrics
# ---------------------------------------------------------

onet = aei[aei["facet"].isin(["onet_task", "onet_task::collaboration"])].copy()

onet = onet[onet["variable"].isin(["automation_pct", "augmentation_pct"])].copy()

# ---------------------------------------------------------
# 3. Clean keys for merging
# ---------------------------------------------------------
# Clean keys
onet["task_key"] = (
    onet["cluster_name"]
    .str.lower()
    .str.strip()
)

task_meta["task_key"] = (
    task_meta["Task"]
    .str.lower()
    .str.strip()
)

# Merge using correct column name
merged = onet.merge(
    task_meta[["task_key", "Task Type"]],
    on="task_key",
    how="left"
)

print("Share of tasks with missing Task Type:", merged["Task Type"].isna().mean())

# Pivot using correct column name
category_stats = (
    merged
    .pivot_table(
        index="Task Type",
        columns="variable",
        values="value",
        aggfunc="mean"
    )
    .reset_index()
)

category_stats["automation_to_augmentation_ratio"] = (
    category_stats["automation_pct"] / category_stats["augmentation_pct"]
)



# ---------------------------------------------------------
# 6. Plot automation vs augmentation by category
# ---------------------------------------------------------

plt.figure(figsize=(10,6))
sns.barplot(
    data=category_stats.melt(
        id_vars="Task_Type",
        value_vars=["automation_pct", "augmentation_pct"],
        var_name="metric",
        value_name="pct"
    ),
    x="Task_Type",
    y="pct",
    hue="metric"
)
plt.xticks(rotation=45, ha="right")
plt.title("Automation vs Augmentation by O*NET Task Category")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 7. Plot automation/augmentation ratio
# ---------------------------------------------------------

plt.figure(figsize=(10,5))
sns.barplot(
    data=category_stats,
    x="Task_Type",
    y="automation_to_augmentation_ratio"
)
plt.xticks(rotation=45, ha="right")
plt.title("Automation/Augmentation Ratio by Task Category")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 8. Identify top automated + top augmented categories
# ---------------------------------------------------------

top_auto = category_stats.sort_values("automation_pct", ascending=False)
top_aug = category_stats.sort_values("augmentation_pct", ascending=False)

print("Top Automated Categories:")
print(top_auto.head(10))

print("\nTop Augmented Categories:")
print(top_aug.head(10))

# ---------------------------------------------------------
# 9. Save results
# ---------------------------------------------------------

category_stats.to_csv("results/task_category_stats.csv", index=False)

print(onet.head())
print(onet["cluster_name"].head())
