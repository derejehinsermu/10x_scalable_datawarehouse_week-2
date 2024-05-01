
import csv
import sys
import pandas as pd

# Increase the maximum CSV field size limit
csv.field_size_limit(sys.maxsize)

# Specify the input and intermediate output file locations
input_file = '../data/dataset.csv'
intermediate_output_file = '../data/intermediate_output_dataset.csv'

# Open the input file for reading and an intermediate output file for writing
with open(input_file, 'r') as infile, open(intermediate_output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter=';')
    writer = csv.writer(outfile)

    # Write only the first 10 columns of each row to the intermediate output file
    for row in reader:
        writer.writerow(row[:10])

# Now, use pandas to load the intermediate output file
df = pd.read_csv(intermediate_output_file, delimiter=',')

# Remove any leading/trailing spaces from column names
df.columns = df.columns.str.strip()


# Split data into trajectories and vehicles based on the cleaned columns
trajectories = df[['track_id', 'lat', 'lon', 'speed', 'lon_acc', 'lat_acc', 'time']]
vehicles = df[['track_id', 'type', 'traveled_d', 'avg_speed']]

# Save the split data as CSV files
trajectories.to_csv('../data/trajectories.csv', index=False)
vehicles.to_csv('../data/vehicles.csv', index=False)
