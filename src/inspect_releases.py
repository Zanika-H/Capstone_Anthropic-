from pathlib import Path
import pandas as pd

FILES = {
    "Feb 2025": Path("data/release_2025_02_10/onet_task_mappings.csv"),
    "Mar 2025": Path("data/release_2025_03_27/task_pct_v1.csv"),
    "Sep 2025": Path("data/release_2025_09_15/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv"),
    "Jan 2026": Path("data/release_2026_01_15/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv"),
    "Mar 2026": Path("data/release_2026_03_24/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv"),
    "Jun 2026": Path("data/release_2026_06_26/aei_claude_ai_2026-06-26.csv"),
}

for release, path in FILES.items():
    print("\n" + "=" * 60)
    print(release)
    print("=" * 60)
    print("File:", path)

    df = pd.read_csv(path, nrows=5)

    print("\nColumns:")
    for column in df.columns:
        print(" -", column)

    print("\nFirst 5 rows:")
    print(df.to_string(index=False))