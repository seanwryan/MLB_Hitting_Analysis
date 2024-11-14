import pandas as pd

# File paths for the batting dataset (assuming we are analyzing batting data first)
file_paths = {
    "Hitting Regular": "../data/raw/hitting_regular.csv",
    "Hitting Postseason": "../data/raw/hitting_post.csv"
}

# Function to explore each dataset with detailed analysis
def explore_data(file_path, name):
    print(f"\n{'='*40}")
    print(f"Exploring {name}")
    print(f"{'='*40}")
    
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Show basic information about the dataset
    print("\nBasic Info:")
    data.info()
    
    # Display the first few rows
    print("\nFirst 5 Rows:")
    print(data.head())
    
    # Check for duplicate rows
    duplicate_rows = data[data.duplicated()]
    print(f"\nTotal Duplicate Rows: {len(duplicate_rows)}")
    
    # Check for partial duplicates based on player identifier (Player-additional)
    partial_duplicates = data[data.duplicated(subset=['Player-additional'], keep=False)]
    print(f"\nTotal Partial Duplicates based on Player-additional: {len(partial_duplicates)}")
    if not partial_duplicates.empty:
        print("\nExample of Partial Duplicates:")
        print(partial_duplicates.head())
    
    # Summarize missing values
    print("\nMissing Values per Column:")
    missing_values = data.isnull().sum()
    print(missing_values[missing_values > 0])
    
    # Check data types and convert as needed
    print("\nData Types:")
    print(data.dtypes)
    
    # Summary statistics for numerical columns
    print("\nSummary Statistics for Numerical Columns:")
    print(data.describe())

    # Identify categorical columns and display unique values
    categorical_columns = data.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        unique_values = data[col].unique()
        print(f"\nUnique values in {col} ({len(unique_values)}): {unique_values[:10]}{'...' if len(unique_values) > 10 else ''}")
    
    # Identify rate vs. counting stats
    rate_stats = ['BA', 'OBP', 'SLG', 'OPS']  # List rate-based stats
    counting_stats = [col for col in data.columns if col not in rate_stats and data[col].dtype != 'object']
    
    print("\nCounting Stats Columns (for summing across duplicates):", counting_stats)
    print("Rate Stats Columns (for recalculation):", rate_stats)

# Loop through each batting file and run the detailed analysis
for name, path in file_paths.items():
    explore_data(path, name)