from pathlib import Path
import pandas as pd


# --------------------------------------------------
# Set project and data locations
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


# --------------------------------------------------
# Load the raw Claude.ai dataset
# --------------------------------------------------

claude_file = DATA_DIR / "aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv"

claude_df = pd.read_csv(claude_file)


# --------------------------------------------------
# Basic dataset information
# --------------------------------------------------

print("=" * 60)
print("CLAUDE.AI DATASET PROFILE")
print("=" * 60)

print(f"\nRows: {len(claude_df):,}")
print(f"Columns: {len(claude_df.columns)}")

print("\nColumns:")
print(claude_df.columns.tolist())


# --------------------------------------------------
# Geographic coverage
# --------------------------------------------------

print("\n" + "=" * 60)
print("GEOGRAPHIC COVERAGE")
print("=" * 60)

print(
    claude_df["geography"]
    .value_counts(dropna=False)
)


# --------------------------------------------------
# Facets
# --------------------------------------------------

print("\n" + "=" * 60)
print("FACETS")
print("=" * 60)

print(
    claude_df["facet"]
    .value_counts(dropna=False)
)


# --------------------------------------------------
# Variables
# --------------------------------------------------

print("\n" + "=" * 60)
print("VARIABLES")
print("=" * 60)

print(
    claude_df["variable"]
    .value_counts(dropna=False)
)


# --------------------------------------------------
# Missing values
# --------------------------------------------------

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing = claude_df.isna().sum()

print(missing)


# --------------------------------------------------
# Plot 1: Geographic coverage
# --------------------------------------------------

import matplotlib.pyplot as plt

geography_counts = claude_df["geography"].value_counts()

plt.figure(figsize=(8, 5))
geography_counts.plot(kind="bar")

plt.title("Claude.ai Dataset Records by Geographic Level")
plt.xlabel("Geographic Level")
plt.ylabel("Number of Records")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("geography_coverage.png", dpi=300)
plt.show()

# --------------------------------------------------
# Plot 2: Records by facet
# --------------------------------------------------

facet_counts = claude_df["facet"].value_counts()

plt.figure(figsize=(10, 6))
facet_counts.plot(kind="bar")

plt.title("Claude.ai Dataset Records by Facet")
plt.xlabel("Facet")
plt.ylabel("Number of Records")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("facet_distribution.png", dpi=300)
plt.show()

# --------------------------------------------------
# Plot 3: Records by variable
# --------------------------------------------------

variable_counts = claude_df["variable"].value_counts()

plt.figure(figsize=(10, 6))
variable_counts.plot(kind="bar")

plt.title("Claude.ai Dataset Records by Variable")
plt.xlabel("Variable")
plt.ylabel("Number of Records")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("variable_distribution.png", dpi=300)
plt.show()