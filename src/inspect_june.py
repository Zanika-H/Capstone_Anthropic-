from pathlib import Path
import pandas as pd

path = Path(
    "data/release_2026_06_26/aei_claude_ai_2026-06-26.csv"
)

df = pd.read_csv(path)

print("=" * 70)
print("JUNE 2026")
print("=" * 70)

print("\nCategory counts:")
print(df["category_name"].value_counts())

print("\n--- ONET TASK RECORDS ---")

onet = df[df["category_name"] == "onet"]

print("Number of rows:", len(onet))

print("\nMetric IDs:")
print(onet["metric_id"].value_counts())

print("\nExample records:")
print(
    onet[
        [
            "category_name",
            "hierarchy_level",
            "metric_id",
            "value",
            "node_name",
            "node_external_id"
        ]
    ].head(10).to_string(index=False)
)

print("\n--- SOC OCCUPATION RECORDS ---")

soc = df[df["category_name"] == "soc_occupation"]

print("Number of rows:", len(soc))

print("\nMetric IDs:")
print(soc["metric_id"].value_counts())

print("\nExample records:")
print(
    soc[
        [
            "category_name",
            "hierarchy_level",
            "metric_id",
            "value",
            "node_name",
            "node_external_id"
        ]
    ].head(10).to_string(index=False)
)