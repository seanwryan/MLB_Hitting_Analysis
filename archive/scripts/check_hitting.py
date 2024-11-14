import pandas as pd

def validate_hitting_data(df):
    # Check that required columns exist
    required_columns = [
        'Player-additional', 'Player', 'Age', 'Team', 'Lg', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 
        'RBI', 'SB', 'CS', 'BB', 'SO', 'TB', 'GIDP', 'HBP', 'SH', 'SF', 'IBB', 'BA', 'OBP', 'SLG', 'OPS', 'Multi_Team'
    ]
    for col in required_columns:
        assert col in df.columns, f"Missing required column: {col}"

    # Check for any null values in essential columns
    essential_columns = ['Player-additional', 'Player', 'Age', 'Team', 'G', 'PA', 'AB', 'R', 'H']
    assert df[essential_columns].notna().all().all(), "Null values found in essential columns."

    # Check that Multi_Team flag is consistent with the Team column
    multi_team_inconsistencies = df[(df['Multi_Team'] != df['Team'].str.contains('/'))]
    if not multi_team_inconsistencies.empty:
        print("Inconsistent Multi_Team flag detected. Sample of inconsistencies:")
        print(multi_team_inconsistencies[['Player', 'Team', 'Multi_Team']].head())
    assert multi_team_inconsistencies.empty, "Inconsistent Multi_Team flag detected."

    # Check that rate stats are within logical bounds
    rate_stats = ['BA', 'OBP', 'SLG']
    for stat in rate_stats:
        assert df[stat].between(0, 1).all(), f"{stat} contains values outside the range 0 to 1."

    # Check for non-negative values in countable stats
    countable_stats = ['G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'TB', 'GIDP', 'HBP', 'SH', 'SF', 'IBB']
    for stat in countable_stats:
        assert (df[stat] >= 0).all(), f"{stat} contains negative values."

    print("All checks passed.")

# Load the cleaned data
df_cleaned_hitting = pd.read_csv('/Users/seanryan/Documents/MLB_Project/data/processed/hitting_regular_cleaned.csv')

# Run validations
validate_hitting_data(df_cleaned_hitting)