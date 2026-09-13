from pathlib import Path
import pandas as pd


# --------------------------------------------------
# Set project and data locations
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


# --------------------------------------------------
# Load the Claude.ai raw dataset
# --------------------------------------------------

claude_file = DATA_DIR / "aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv"

claude_df = pd.read_csv(claude_file)


# --------------------------------------------------
# Display 5 raw examples
# --------------------------------------------------

print("=" * 60)
print("5 RAW CLAUDE.AI EXAMPLES")
print("=" * 60)

examples = claude_df.iloc[100:105]

print(
    examples.to_string(index=False)
)