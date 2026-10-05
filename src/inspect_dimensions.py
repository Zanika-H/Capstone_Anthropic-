from pathlib import Path
import pandas as pd


FILES = {
    "Sep 2025": (
        Path("data/release_2025_09_15/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv"),
        ["facet", "level", "variable", "cluster_name", "platform_and_product"]
    ),
    "Jan 2026": (
        Path("data/release_2026_01_15/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv"),
        ["facet", "level", "variable", "cluster_name", "platform_and_product"]
    ),
    "Mar 2026": (
        Path("data/release_2026_03_24/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv"),
        ["facet", "level", "variable", "cluster_name", "platform_and_product"]
    ),
    "Jun 2026": (
        Path("data/release_2026_06_26/aei_claude_ai_2026-06-26.csv"),
        ["category_name", "hierarchy_level", "metric_id"]
    ),
}


for release, (path, columns) in FILES.items():

    print("\n" + "=" * 70)
    print(release)
    print("=" * 70)

    for chunk in pd.read_csv(path, usecols=columns, chunksize=50000):

        for column in columns:
            values = chunk[column].dropna().unique()

            print(f"\n{column}:")
            print(values[:30])

        break