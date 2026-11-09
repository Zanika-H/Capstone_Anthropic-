
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

print("PERCENTAGE COMPARABILITY DIAGNOSTIC")
print("-----------------------------------")

for period in periods:
    values = df[period]

    print(f"\n{period}")
    print("Sum of reported percentages:", round(values.sum(), 4))
    print("Mean percentage:", round(values.mean(), 4))
    print("Median percentage:", round(values.median(), 4))
    print("Nonzero task percentages:", (values > 0).sum())
    print("Tasks >= 1%:", (values >= 1).sum())

print("\nTOP 5 TASKS BY PERIOD")

for period in periods:
    print(f"\n{period}")

    print(
        df.nlargest(5, period)[
            ["task_key", period]
        ].to_string(index=False)
    )
