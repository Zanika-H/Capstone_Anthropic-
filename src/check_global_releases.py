
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]

files = {
    "September 2025": (
        "release_2025_09_15",
        "aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv"
    ),
    "January 2026": (
        "release_2026_01_15",
        "aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv"
    ),
    "March 2026": (
        "release_2026_03_24",
        "aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv"
    )
}

for release, (folder, filename) in files.items():
    path = PROJECT_DIR / "data" / folder / filename

    print(f"\n--- {release} ---")

    if not path.exists():
        print("FILE NOT FOUND:", path)
        continue

    df = pd.read_csv(path, low_memory=False)

    # Keep only task percentage records
    tasks = df[
        (df["facet"] == "onet_task")
        & (df["variable"] == "onet_task_pct")
    ].copy()

    print("Total task percentage rows:", len(tasks))
    print("Available geo_id examples:", tasks["geo_id"].dropna().unique()[:10])

    global_tasks = tasks[tasks["geo_id"] == "GLOBAL"]

    print("Global task rows:", len(global_tasks))
    print("Unique global task names:", global_tasks["cluster_name"].nunique())
    print("Missing percentage values:", global_tasks["value"].isna().sum())

    print("Collection dates:")
    print(
        global_tasks[["date_start", "date_end"]]
        .drop_duplicates()
        .to_string(index=False)
    )
