from pathlib import Path
import pandas as pd


# Find the project folder
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Location of the data
DATA_DIR = PROJECT_ROOT / "data"


def inventory_file(file_path):
    print("=" * 80)
    print(f"FILE: {file_path.name}")
    print("=" * 80)

    # File size
    size_mb = file_path.stat().st_size / (1024 * 1024)
    print(f"File size: {size_mb:.2f} MB")

    # Read the CSV
    df = pd.read_csv(file_path)

    # Number of rows and columns
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    # Column names and data types
    print("\nColumns and data types:")
    for column in df.columns:
        print(f"  {column}: {df[column].dtype}")

    # Missing values
    print("\nMissing values:")
    missing = df.isna().sum()
    missing_percent = (df.isna().mean() * 100).round(2)

    missing_table = pd.DataFrame({
        "Missing Count": missing,
        "Missing Percent": missing_percent
    })

    print(missing_table)

    print("\n")


# Check that the data folder exists
if not DATA_DIR.exists():
    print(f"Data folder not found: {DATA_DIR}")
    exit()


# Find all files in the data folder
all_files = sorted(DATA_DIR.iterdir())

print("=" * 80)
print("DATASET INVENTORY")
print("=" * 80)

if not all_files:
    print("No files found in the data folder.")
else:
    print(f"Found {len(all_files)} file(s) in the data folder.\n")

    # Show every file
    print("Files:")
    for file_path in all_files:
        if file_path.is_file():
            size_mb = file_path.stat().st_size / (1024 * 1024)
            print(f"  {file_path.name} - {size_mb:.2f} MB")

    print("\n")

    # Inventory CSV files
    csv_files = sorted(DATA_DIR.glob("*.csv"))

    print(f"CSV files found: {len(csv_files)}\n")

    if not csv_files:
        print("No CSV files found.")
    else:
        for file_path in csv_files:
            inventory_file(file_path)