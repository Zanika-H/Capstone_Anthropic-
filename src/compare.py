import pandas as pd

jan = pd.read_csv(
    "data/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv"
)

print("Shape:")
print(jan.shape)

print("\nColumns:")
print(jan.columns)

print("\nFirst 5 rows:")
print(jan.head())