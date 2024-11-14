import pandas as pd

def clean_hitting_data(df, is_postseason=False):
    # Filter out players with fewer than 30 plate appearances
    df = df[df['PA'] >= 30].copy()

    # Rounding rate statistics to 3 decimal places
    rate_stats = ['BA', 'OBP', 'SLG', 'OPS']
    df[rate_stats] = df[rate_stats].round(3)

    if not is_postseason:
        # Add Multi_Team flag for identifying players with "2TM" or "3TM" entries
        df['Multi_Team'] = df['Team'].str.contains(r'\b\d+TM\b', regex=True)

        # Process players with multiple teams
        multi_team_players = df[df['Multi_Team']].copy()
        single_team_entries = df[~df['Multi_Team']]

        # For each player in multi_team_players, consolidate team names
        for player_id in multi_team_players['Player-additional'].unique():
            # Get the multi-team entry and the individual team entries for this player
            multi_team_entry = multi_team_players[multi_team_players['Player-additional'] == player_id]
            individual_team_entries = single_team_entries[single_team_entries['Player-additional'] == player_id]

            if not multi_team_entry.empty and not individual_team_entries.empty:
                # Concatenate all individual teams and update the multi-team entry's 'Team' column
                teams = '/'.join(sorted(individual_team_entries['Team'].unique()))
                df.loc[multi_team_entry.index, 'Team'] = teams

                # Remove individual team entries for this player from df
                df = df.drop(individual_team_entries.index)

    # Drop Pos column as it's not crucial for analysis
    if 'Pos' in df.columns:
        df = df.drop(columns=['Pos'])

    # Aggregate the data, grouping by Player-additional for unique players
    combined_df = df.groupby('Player-additional').agg({
        'Player': 'first',
        'Age': 'mean',
        'Team': 'first',  # Team is already consolidated for multi-team players
        'Lg': 'first',
        'G': 'sum',
        'PA': 'sum',
        'AB': 'sum',
        'R': 'sum',
        'H': 'sum',
        '2B': 'sum',
        '3B': 'sum',
        'HR': 'sum',
        'RBI': 'sum',
        'SB': 'sum',
        'CS': 'sum',
        'BB': 'sum',
        'SO': 'sum',
        'TB': 'sum',
        'GIDP': 'sum',
        'HBP': 'sum',
        'SH': 'sum',
        'SF': 'sum',
        'IBB': 'sum',
        'BA': lambda x: (x * df.loc[x.index, 'AB']).sum() / df.loc[x.index, 'AB'].sum(),
        'OBP': lambda x: (x * df.loc[x.index, 'PA']).sum() / df.loc[x.index, 'PA'].sum(),
        'SLG': lambda x: (x * df.loc[x.index, 'AB']).sum() / df.loc[x.index, 'AB'].sum(),
        'OPS': lambda x: (x * df.loc[x.index, 'PA']).sum() / df.loc[x.index, 'PA'].sum(),
    }).reset_index()

    # Round the final SLG and OPS values to 3 decimal places
    combined_df['BA'] = combined_df['BA'].round(3)
    combined_df['OBP'] = combined_df['OBP'].round(3)
    combined_df['SLG'] = combined_df['SLG'].round(3)
    combined_df['OPS'] = combined_df['OPS'].round(3)

    return combined_df

# Load regular season data
df_regular = pd.read_csv('/Users/seanryan/Documents/MLB_Project/data/raw/hitting_regular.csv')
# Clean regular season data
cleaned_regular_df = clean_hitting_data(df_regular)
# Save cleaned regular season data
cleaned_regular_df.to_csv('/Users/seanryan/Documents/MLB_Project/data/processed/hitting_regular_cleaned.csv', index=False)

# Load postseason data
df_post = pd.read_csv('/Users/seanryan/Documents/MLB_Project/data/raw/hitting_post.csv')
# Clean postseason data
cleaned_post_df = clean_hitting_data(df_post, is_postseason=True)
# Save cleaned postseason data
cleaned_post_df.to_csv('/Users/seanryan/Documents/MLB_Project/data/processed/hitting_post_cleaned.csv', index=False)