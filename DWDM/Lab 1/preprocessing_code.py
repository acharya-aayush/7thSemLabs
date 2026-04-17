import pandas as pd

# Load the primary dataset
primary_file_path = "d:/Aayush_Acharya/7th Sem/DWDM/Lab 1/barcelona_players.csv"
primary_df = pd.read_csv(primary_file_path)

# Load the secondary dataset
secondary_file_path = "d:/Aayush_Acharya/7th Sem/DWDM/Lab 1/secondary_dataset.csv"
secondary_df = pd.read_csv(secondary_file_path)

# Clean the primary dataset
primary_df_cleaned = primary_df.dropna()

# Clean the secondary dataset
secondary_df_cleaned = secondary_df.dropna()

# Combine the cleaned datasets
combined_df = pd.merge(primary_df_cleaned, secondary_df_cleaned, left_on="player_id", right_on="match_id", how="outer")

print("Cleaned Dataset:")
print(combined_df)