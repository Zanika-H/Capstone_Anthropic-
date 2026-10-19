
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Project folders
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
FIGURES_DIR = ROOT / "figures"

FIGURES_DIR.mkdir(exist_ok=True)

# -------------------------------------------------
# 1. Unique task names across AEI releases
# -------------------------------------------------
# These counts came from our earlier exploratory
# analysis of the datasets.
# Note: They are not directly comparable because
# dataset structure and task hierarchy differ.

release_names = [
    "Feb 2025",
    "Mar 2025",
    "Sep 2025",
    "Jan 2026",
    "Mar 2026",
    "Jun 2026",
]

unique_tasks = [3514, 3365, 2618, 3170, 3260, 3846]

plt.figure(figsize=(10, 5))
bars = plt.bar(release_names, unique_tasks)

plt.title("Unique O*NET Task Names Across AEI Releases")
plt.xlabel("AEI Release")
plt.ylabel("Number of Unique Task Names")
plt.xticks(rotation=30, ha="right")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 25,
        f"{int(bar.get_height()):,}",
        ha="center",
    )

plt.ylim(0, 4200)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "task_counts_by_release.png", dpi=300)
plt.close()


# -------------------------------------------------
# 2. Load June 2026 dataset
# -------------------------------------------------

june_file = (
    DATA_DIR
    / "release_2026_06_26"
    / "aei_claude_ai_2026-06-26.csv"
)

df = pd.read_csv(june_file, low_memory=False)

# Keep global, task-level O*NET percentages
tasks = df[
    (df["category_name"] == "onet")
    & (df["metric_id"] == "pct")
    & (df["hierarchy_level"] == 0)
    & (df["geo_id"] == "GLOBAL")
].copy()

tasks["node_external_id"] = (
    tasks["node_external_id"].astype("string")
)

# Check for duplicate month/task combinations
duplicates = tasks.duplicated(
    ["date_start", "node_external_id"]
).sum()

if duplicates:
    raise ValueError(
        f"Found {duplicates} duplicate month/task IDs."
    )

# Separate April and May task IDs
april = set(
    tasks.loc[
        tasks["date_start"] == "2026-04-01",
        "node_external_id",
    ].dropna()
)

may = set(
    tasks.loc[
        tasks["date_start"] == "2026-05-01",
        "node_external_id",
    ].dropna()
)

shared = april & may
april_only = april - may
may_only = may - april

print("April task IDs:", len(april))
print("May task IDs:", len(may))
print("Shared task IDs:", len(shared))
print("April only:", len(april_only))
print("May only:", len(may_only))


# -------------------------------------------------
# 3. April vs May published task counts
# -------------------------------------------------

months = ["April 2026", "May 2026"]
counts = [len(april), len(may)]

plt.figure(figsize=(7, 5))
bars = plt.bar(months, counts)

plt.title("Published Global O*NET Tasks: April vs May 2026")
plt.ylabel("Number of Unique Task IDs")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 25,
        f"{int(bar.get_height()):,}",
        ha="center",
    )

plt.ylim(0, max(counts) * 1.15)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "april_may_task_counts.png", dpi=300)
plt.close()


# -------------------------------------------------
# 4. Task ID overlap between April and May
# -------------------------------------------------

categories = ["Shared", "April Only", "May Only"]
overlap_counts = [
    len(shared),
    len(april_only),
    len(may_only),
]

plt.figure(figsize=(8, 5))
bars = plt.bar(categories, overlap_counts)

plt.title("O*NET Task ID Overlap: April vs May 2026")
plt.ylabel("Number of Task IDs")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 20,
        f"{int(bar.get_height()):,}",
        ha="center",
    )

plt.ylim(0, max(overlap_counts) * 1.15)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "april_may_task_overlap.png", dpi=300)
plt.close()

print("\nEDA charts saved to:", FIGURES_DIR)
