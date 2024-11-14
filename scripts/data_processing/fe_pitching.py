import pandas as pd

def engineer_pitching_features(df):
    # Avoid division by zero by adding a small constant where necessary

    # Strikeout Rate (K%) and Walk Rate (BB%)
    df['K%'] = df['SO'] / df['BF']
    df['BB%'] = df['BB'] / df['BF']

    # Strikeout-to-Walk Ratio (K/BB)
    df['K/BB'] = (df['SO'] / df['BB']).replace([float('inf'), -float('inf')], 0).fillna(0)

    # Home Runs per 9 Innings (HR9)
    df['HR9'] = df['HR'] / df['IP'] * 9

    # Hits per 9 Innings (H9) and Walks per 9 Innings (BB9) and Strikeouts per 9 Innings (K9)
    df['H9'] = df['H'] / df['IP'] * 9
    df['BB9'] = df['BB'] / df['IP'] * 9
    df['K9'] = df['SO'] / df['IP'] * 9

    # WHIP (Walks + Hits per Inning Pitched)
    df['WHIP'] = (df['BB'] + df['H']) / df['IP']

    # FIP (Fielding Independent Pitching) - Simplified as we may lack advanced stats like HBP and IBB weights
    # Using an approximation of FIP with HR, BB, SO, IP
    # FIP = (13*HR + 3*BB - 2*SO) / IP + Constant (constant generally set to around 3.1 for approximation)
    df['FIP'] = ((13 * df['HR'] + 3 * df['BB'] - 2 * df['SO']) / df['IP']).fillna(0) + 3.1

    # Rounding all new features to 3 decimal places for consistency
    df = df.round({
        'K%': 3,
        'BB%': 3,
        'K/BB': 3,
        'HR9': 3,
        'H9': 3,
        'BB9': 3,
        'K9': 3,
        'WHIP': 3,
        'FIP': 3
    })
    
    return df

# Load cleaned data
df_cleaned_pitching_regular = pd.read_csv('/Users/seanryan/Documents/MLB_Project/data/processed/pitching_regular_cleaned.csv')
df_cleaned_pitching_post = pd.read_csv('/Users/seanryan/Documents/MLB_Project/data/processed/pitching_post_cleaned.csv')

# Engineer features for regular season
df_regular_with_features = engineer_pitching_features(df_cleaned_pitching_regular)
df_regular_with_features.to_csv('/Users/seanryan/Documents/MLB_Project/data/processed/pitching_regular_with_features.csv', index=False)

# Engineer features for post season
df_post_with_features = engineer_pitching_features(df_cleaned_pitching_post)
df_post_with_features.to_csv('/Users/seanryan/Documents/MLB_Project/data/processed/pitching_post_with_features.csv', index=False)

print("Feature engineering complete. Enhanced datasets saved for both regular and postseason.")