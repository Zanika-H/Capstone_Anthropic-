from pathlib import Path
import pandas as pd

FILES = {
    "Feb 2025": (
        Path("data/release_2025_02_10/onet_task_mappings.csv"),
        "task_name"
    ),
    "Mar 2025": (
        Path("data/release_2025_03_27/task_pct_v2.csv"),
        "task_name"
    ),
    "Sep 2025": (
        Path("data/release_2025_09_15/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv"),
        "cluster_name"
    ),
    "Jan 2026": (
        Path("data/release_2026_01_15/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv"),
        "cluster_name"
    ),
    "Mar 2026": (
        Path("data/release_2026_03_24/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv"),
        "cluster_name"
    ),
}

task_sets = {}

for release, (path, column) in FILES.items():

    print("\n" + "=" * 60)
    print(release)
    print("=" * 60)

    if release in ["Sep 2025", "Jan 2026", "Mar 2026"]:

        df = pd.read_csv(
            path,
            usecols=["facet", "cluster_name"],
            on_bad_lines="skip",
            low_memory=False
        )

        df = df[df["facet"] == "onet_task"]
        tasks = set(df["cluster_name"].dropna())

    else:

        df = pd.read_csv(path, usecols=[column])
        tasks = set(df[column].dropna())

    task_sets[release] = tasks

    print("Number of unique tasks:", len(tasks))


print("\n" + "=" * 60)
print("TASK OVERLAP")
print("=" * 60)

releases = list(task_sets.keys())

for i in range(len(releases)):
    for j in range(i + 1, len(releases)):

        release_a = releases[i]
        release_b = releases[j]

        shared = task_sets[release_a] & task_sets[release_b]

        print(
            f"{release_a} vs {release_b}: "
            f"{len(shared)} shared tasks"
        )
 # June 2026
june = pd.read_csv(
    "data/release_2026_06_26/aei_claude_ai_2026-06-26.csv",
    low_memory=False
)

# Keep only O*NET task percentage records
june_tasks = june[
    (june["category_name"] == "onet") &
    (june["metric_id"] == "pct")
]

# Get unique task names
# Get June task names using consistent formatting
june_task_names = set(
    june_tasks["node_name"]
    .dropna()
    .astype(str)
    .str.strip()
    .str.lower()
)

print("June 2026 unique tasks:", len(june_task_names))

# Compare June 2026 with the earlier releases
print("\n" + "=" * 60)
print("JUNE 2026 TASK OVERLAP")
print("=" * 60)

for release_name, task_names in task_sets.items():
    shared = june_task_names & task_names
    print(f"{release_name} vs Jun 2026: {len(shared)} shared tasks")