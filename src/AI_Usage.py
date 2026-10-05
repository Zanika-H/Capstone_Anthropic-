import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ---------------------------------------------------------
# 1. Load AEI dataset
# ---------------------------------------------------------
aei = pd.read_csv("data/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv")

# ---------------------------------------------------------
# 2. Filter to occupation-level data
# ---------------------------------------------------------
occ = aei[aei["facet"] == "soc_occupation"].copy()

print("Rows in occupation dataset:", len(occ))
print(occ.head())

# ---------------------------------------------------------
# ---------------------------------------------------------
# 3. Pivot to get soc_pct per occupation
# ---------------------------------------------------------
occ_stats = (
    occ
    .pivot_table(
        index="cluster_name",
        columns="variable",
        values="value",
        aggfunc="mean"
    )
    .reset_index()
)

print("\nPivoted occupation stats:")
print(occ_stats.head())

# ---------------------------------------------------------
# 4. Outlier Detection 
# ---------------------------------------------------------
q1 = occ_stats["soc_pct"].quantile(0.25)
q3 = occ_stats["soc_pct"].quantile(0.75)
iqr = q3 - q1

upper = q3 + 1.5 * iqr
lower = q1 - 1.5 * iqr

outliers = occ_stats[(occ_stats["soc_pct"] > upper) | (occ_stats["soc_pct"] < lower)]

print("\nOutlier Occupations:")
print(outliers)


# ---------------------------------------------------------
# 5. Plot top 20 occupations
# ---------------------------------------------------------
plt.figure(figsize=(12, 6))
sns.barplot(
    data=top_occ.head(20),
    x="cluster_name",
    y="soc_pct",
    palette="viridis"
)
plt.xticks(rotation=45, ha="right")
plt.title("Top 20 Occupations by AI Penetration (soc_pct)")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 6. Save results
# ---------------------------------------------------------
top_occ.to_csv("results/top_occupations_by_soc_pct.csv", index=False)

print("\nSaved: results/top_occupations_by_soc_pct.csv")

plt.figure(figsize=(10,6))
sns.histplot(occ_stats["soc_pct"], bins=30, kde=True)
plt.title("Distribution of AI Penetration Across Occupations")
plt.xlabel("soc_pct")
plt.ylabel("Count")
plt.show()

bottom_occ = occ_stats.sort_values("soc_pct", ascending=True)
print(bottom_occ.head(20))

group_stats = (
    occ_stats
    .groupby("cluster_name")["soc_pct"]
    .mean()
    .sort_values(ascending=False)
)

print(group_stats)

plt.figure(figsize=(12,6))
sns.barplot(
    x=group_stats.index,
    y=group_stats.values,
    palette="magma"
)
plt.xticks(rotation=45, ha="right")
plt.title("Average AI Penetration by Occupation Group")
plt.tight_layout()
plt.show()

q1 = occ_stats["soc_pct"].quantile(0.25)
q3 = occ_stats["soc_pct"].quantile(0.75)
iqr = q3 - q1

upper = q3 + 1.5 * iqr
lower = q1 - 1.5 * iqr

outliers = occ_stats[(occ_stats["soc_pct"] > upper) | (occ_stats["soc_pct"] < lower)]
print(outliers)

country = aei[aei["facet"] == "country"].copy()

country_stats = (
    country
    .pivot_table(
        index="geo_name",
        columns="variable",
        values="value",
        aggfunc="mean"
    )
    .reset_index()
)

print(country_stats.head())

plt.figure(figsize=(10,6))
sns.scatterplot(
    data=occ_stats,
    x="soc_pct",
    y="soc_pct",  # placeholder until we merge with country data
    hue="cluster_name"
)
plt.title("AI Penetration Patterns")
plt.show()


