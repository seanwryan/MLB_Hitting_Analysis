import pandas as pd

# Load the dataset
data = pd.read_csv("/Users/seanryan/Documents/MLB_Project/data/processed/hitting_clustered_refined.csv")

# Define the 40-man roster player names (as clean as possible)
roster_players = [
    "Alek Thomas", "Randal Grichuk", "Eugenio Suárez", "Kevin Newman", "Geraldo Perdomo", 
    "Gabriel Moreno", "Corbin Carroll", "Christian Walker", "Lourdes Gurriel Jr.", "Jake McCarthy", 
    "Joc Pederson", "Pavin Smith", "Josh Bell", "José Herrera", "Ketel Marte", 
    "Adrian Del Castillo", "Jorge Barrosa", "Jordan Lawlar", "Blaze Alexander"
]

# Function to clean player names by removing special characters and extra spaces
def clean_name(name):
    name = name.replace("#", "").replace("*", "").strip()  # Remove symbols and extra spaces
    return name

# Apply cleaning function to the "Player" column in the data
data['Player'] = data['Player'].apply(clean_name)

# Filter data to keep only rows where "Player" is in the roster_players list
filtered_data = data[data['Player'].isin(roster_players)]

# Save the filtered data to a new CSV file
filtered_data.to_csv("/Users/seanryan/Documents/MLB_Project/data/processed/diamondbacks_hitting_clustered_refined.csv", index=False)

# Display the filtered data for verification
print(filtered_data.head())