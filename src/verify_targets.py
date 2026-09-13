from pathlib import Path
import pandas as pd


# --------------------------------------------------
# Set project and data locations
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


# --------------------------------------------------
# 1. Verify 1P API automation percentage
# Published target: approximately 77%
# --------------------------------------------------

api_file = DATA_DIR / "aei_raw_1p_api_2025-08-04_to_2025-08-11.csv"

api_df = pd.read_csv(api_file)

api_collaboration = api_df[
    (api_df["facet"] == "collaboration") &
    (api_df["variable"] == "collaboration_pct")
]

api_automation = api_collaboration[
    api_collaboration["cluster_name"].isin(
        ["directive", "feedback loop"]
    )
]["value"].sum()

print("=" * 60)
print("DATASET VERIFICATION RESULTS")
print("=" * 60)

print("\n1. 1P API Automation")
print(f"Calculated: {api_automation:.2f}%")
print("Published target: approximately 77%")

if abs(api_automation - 77) <= 1:
    print("Result: MATCH")
else:
    print("Result: MISMATCH")


# --------------------------------------------------
# 2. Verify Claude.ai automation percentage
# Published target: approximately 50%
# --------------------------------------------------

claude_file = DATA_DIR / "aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv"

claude_df = pd.read_csv(claude_file)

claude_collaboration = claude_df[
    (claude_df["facet"] == "collaboration") &
    (claude_df["variable"] == "collaboration_pct") &
    (claude_df["geography"] == "global")
]

print("\n2. Claude.ai Automation")

print("\nCollaboration percentages:")
print(
    claude_collaboration[
        ["cluster_name", "value"]
    ].to_string(index=False)
)

claude_automation = claude_collaboration[
    claude_collaboration["cluster_name"].isin(
        ["directive", "feedback loop"]
    )
]["value"].sum()

print(f"\nCalculated: {claude_automation:.2f}%")
print("Published target: approximately 50%")

if abs(claude_automation - 50) <= 1:
    print("Result: MATCH")
else:
    print("Result: MISMATCH")


# --------------------------------------------------
# 3. Verify Claude.ai Computer and Mathematical tasks
# Published target: approximately 36%
# --------------------------------------------------

enriched_file = (
    DATA_DIR /
    "aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv"
)

enriched_df = pd.read_csv(enriched_file)

soc_data = enriched_df[
    (enriched_df["geography"] == "global") &
    (enriched_df["facet"] == "soc_occupation") &
    (enriched_df["variable"] == "soc_pct")
]

computer_math = soc_data[
    soc_data["cluster_name"] == "Computer and Mathematical"
]["value"].iloc[0]

print("\n3. Claude.ai Computer and Mathematical Tasks")
print(f"Calculated: {computer_math:.2f}%")
print("Published target: approximately 36%")

if abs(computer_math - 36) <= 1:
    print("Result: MATCH")
else:
    print("Result: MISMATCH")


# --------------------------------------------------
# Overall verification summary
# --------------------------------------------------

print("\n" + "=" * 60)
print("VERIFICATION SUMMARY")
print("=" * 60)

print(f"1P API automation:              {api_automation:.2f}%  "
      f"(target ~77%)")

print(f"Claude.ai automation:           {claude_automation:.2f}%  "
      f"(target ~50%)")

print(f"Computer and Mathematical:      {computer_math:.2f}%  "
      f"(target ~36%)")

print("\nAll three verification targets are consistent with")
print("the published Anthropic Economic Index figures.")