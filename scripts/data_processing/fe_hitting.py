import pandas as pd

def engineer_features(df):
    # Calculate SB% (Stolen Base Success Rate)
    df['SB%'] = df.apply(lambda x: x['SB'] / (x['SB'] + x['CS']) if (x['SB'] + x['CS']) > 0 else 0, axis=1).round(3)
    
    # Power Ratio (ISO - Isolated Power)
    df['ISO'] = (df['SLG'] - df['BA']).round(3)
    
    # Contact Quality (BABIP - Batting Average on Balls In Play)
    df['BABIP'] = ((df['H'] - df['HR']) / (df['AB'] - df['SO'] - df['HR'] + df['SF']).replace(0, 1)).round(3)
    
    # Plate Discipline Ratios
    df['BB%'] = (df['BB'] / df['PA']).round(3)
    df['SO%'] = (df['SO'] / df['PA']).round(3)
    df['BB/SO'] = (df['BB'] / df['SO']).replace([float('inf'), -float('inf')], 0).round(3)
    
    # Power-to-Speed Metric (HR/SB Ratio)
    df['HR/SB'] = (df['HR'] / df['SB']).replace([float('inf'), -float('inf')], 0).round(3)
    
    # Extra-Base Hit Rate (XBH%)
    df['XBH%'] = ((df['2B'] + df['3B'] + df['HR']) / df['H']).round(3)
    
    # Run Production Metrics
    df['RBI Rate'] = (df['RBI'] / df['PA']).round(3)
    df['R Rate'] = (df['R'] / df['PA']).round(3)
    
    return df

# Load cleaned data
df_cleaned_hitting_regular = pd.read_csv('/Users/seanryan/Documents/MLB_Project/data/processed/hitting_regular_cleaned.csv')
df_cleaned_hitting_post = pd.read_csv('/Users/seanryan/Documents/MLB_Project/data/processed/hitting_post_cleaned.csv')

# Engineer features for regular season
df_regular_with_features = engineer_features(df_cleaned_hitting_regular)
df_regular_with_features.to_csv('/Users/seanryan/Documents/MLB_Project/data/processed/hitting_regular_with_features.csv', index=False)

# Engineer features for postseason
df_post_with_features = engineer_features(df_cleaned_hitting_post)
df_post_with_features.to_csv('/Users/seanryan/Documents/MLB_Project/data/processed/hitting_post_with_features.csv', index=False)

print("Feature engineering complete. Enhanced datasets saved for both regular and postseason.")