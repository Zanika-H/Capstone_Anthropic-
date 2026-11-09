
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]

df = pd.read_csv(
    PROJECT_DIR / "outputs" /
    "five_period_task_dataset.csv"
)

periods = [
    "aug_2025_pct",
    "nov_2025_pct",
    "feb_2026_pct",
    "apr_2026_pct",
    "may_2026_pct"
]

print("LONGITUDINAL DATA QUALITY CHECK")
print("--------------------------------")
print("Total tasks:", len(df))
print("Duplicate task names:", df["task_key"].duplicated().sum())
print("Missing values:", df[periods].isna().sum().sum())

print("\nPERCENTAGE SUMMARY BY PERIOD")
print(
    df[periods].agg(
        ["min", "max", "mean", "median"]
    ).round(4).to_string()
)

print("\nZERO VALUES BY PERIOD")
for period in periods:
    print(
        period,
        ":",
        (df[period] == 0).sum()
    )

print("\nTASKS WITH LARGE FEBRUARY–APRIL DIFFERENCES")
df["feb_to_apr_pp"] = (
    df["apr_2026_pct"] - df["feb_2026_pct"]
)

print(
    df.reindex(
        df["feb_to_apr_pp"].abs()
        .sort_values(ascending=False).index
    )[
        ["task_key", "feb_2026_pct",
         "apr_2026_pct", "feb_to_apr_pp"]
    ].head(10).to_string(index=False)
)
