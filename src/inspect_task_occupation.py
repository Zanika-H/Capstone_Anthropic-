from pathlib import Path
import pandas as pd


FILES = {
    "Sep 2025": Path(
        "data/release_2025_09_15/"
        "aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv"
    ),
    "Jan 2026": Path(
        "data/release_2026_01_15/"
        "aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv"
    ),
    "Mar 2026": Path(
        "data/release_2026_03_24/"
        "aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv"
    ),
}


for release, path in FILES.items():

    print("\n" + "=" * 70)
    print(release)
    print("=" * 70)

    df = pd.read_csv(path)

    # Look at task-level records
    task = df[df["facet"] == "onet_task"]

    print("\n--- ONET TASK RECORDS ---")
    print("Number of rows:", len(task))

    print("\nVariables:")
    print(task["variable"].value_counts())

    print("\nExample task records:")
    print(
        task[
            ["facet", "level", "variable", "cluster_name", "value"]
        ].head(10).to_string(index=False)
    )

    # Look at occupation-level records
    occupation = df[df["facet"] == "soc_occupation"]

    print("\n--- SOC OCCUPATION RECORDS ---")
    print("Number of rows:", len(occupation))

    print("\nVariables:")
    print(occupation["variable"].value_counts())

    print("\nExample occupation records:")
    print(
        occupation[
            ["facet", "level", "variable", "cluster_name", "value"]
        ].head(10).to_string(index=False)
    )