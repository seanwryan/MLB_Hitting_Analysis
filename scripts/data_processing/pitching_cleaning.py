import pandas as pd

def clean_pitching_data(df, is_postseason=False):
    # Filter out pitchers with fewer than 5 innings pitched
    df = df[df['IP'] >= 5].copy()

    if not is_postseason:
        # Add Multi_Team flag based on "2TM", "3TM", etc., in Team column
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

    # Define aggregation dictionary
    agg_dict = {
        'Player': 'first',
        'Age': 'mean',
        'Team': 'first',  # Consolidate team names
        'Lg': 'first',
        'W': 'sum',
        'L': 'sum',
        'W-L%': 'mean',
        'ERA': lambda x: (x * df.loc[x.index, 'IP']).sum() / df.loc[x.index, 'IP'].sum(),
        'G': 'sum',
        'GS': 'sum',
        'GF': 'sum',
        'CG': 'sum',
        'SHO': 'sum',
        'SV': 'sum',
        'IP': 'sum',
        'H': 'sum',
        'R': 'sum',
        'ER': 'sum',
        'HR': 'sum',
        'BB': 'sum',
        'IBB': 'sum',
        'SO': 'sum',
        'HBP': 'sum',
        'BK': 'sum',
        'WP': 'sum',
        'BF': 'sum',
        'FIP': lambda x: (x * df.loc[x.index, 'IP']).sum() / df.loc[x.index, 'IP'].sum(),
        'WHIP': lambda x: (x * df.loc[x.index, 'IP']).sum() / df.loc[x.index, 'IP'].sum(),
        'H9': lambda x: (x * df.loc[x.index, 'IP']).sum() / df.loc[x.index, 'IP'].sum(),
        'HR9': lambda x: (x * df.loc[x.index, 'IP']).sum() / df.loc[x.index, 'IP'].sum(),
        'BB9': lambda x: (x * df.loc[x.index, 'IP']).sum() / df.loc[x.index, 'IP'].sum(),
        'SO9': lambda x: (x * df.loc[x.index, 'IP']).sum() / df.loc[x.index, 'IP'].sum(),
        'SO/BB': lambda x: (x * df.loc[x.index, 'IP']).sum() / df.loc[x.index, 'IP'].sum(),
    }

    # Conditionally add 'ERA+' and 'WAR' if they are present in the data
    if 'ERA+' in df.columns:
        agg_dict['ERA+'] = 'mean'
    if 'WAR' in df.columns:
        agg_dict['WAR'] = 'sum'

    # Aggregate the data
    combined_df = df.groupby('Player-additional').agg(agg_dict).reset_index()

    # Round the calculated statistics to 3 decimal places
    combined_df[['ERA', 'FIP', 'WHIP', 'H9', 'HR9', 'BB9', 'SO9', 'SO/BB']] = combined_df[
        ['ERA', 'FIP', 'WHIP', 'H9', 'HR9', 'BB9', 'SO9', 'SO/BB']
    ].round(3)

    return combined_df

# Load regular season data
df_regular = pd.read_csv('/Users/seanryan/Documents/MLB_Project/data/raw/pitching_regular.csv')
# Clean regular season data
cleaned_regular_df = clean_pitching_data(df_regular)
# Save cleaned regular season data
cleaned_regular_df.to_csv('/Users/seanryan/Documents/MLB_Project/data/processed/pitching_regular_cleaned.csv', index=False)

# Load postseason data
df_post = pd.read_csv('/Users/seanryan/Documents/MLB_Project/data/raw/pitching_post.csv')
# Clean postseason data
cleaned_post_df = clean_pitching_data(df_post, is_postseason=True)
# Save cleaned postseason data
cleaned_post_df.to_csv('/Users/seanryan/Documents/MLB_Project/data/processed/pitching_post_cleaned.csv', index=False)