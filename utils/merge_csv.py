import pandas as pd

# Read trajectories.csv and vehicles.csv into pandas DataFrames
trajectories_df = pd.read_csv('../data/trajectories.csv')
vehicles_df = pd.read_csv('../data/vehicles.csv')

# Merge the DataFrames based on the common column 'track_id'
merged_df = pd.merge(trajectories_df, vehicles_df, on='track_id', how='inner')

# Now, merged_df contains the merged data from both CSV files based on the 'track_id' column
merged_df.to_csv('../data/clean_dataset.csv')