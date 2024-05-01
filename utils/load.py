import pandas as pd
from sqlalchemy import create_engine

# Path to the CSV file
csv_file_path = '../data/clean_dataset.csv'

database_name = 'vehicle_tracking_data'

# Connection parameters
connection_params = {
    "host": "localhost",
    "user": "postgres",
    "password": "dere",
    "port": "5432",
    "database": database_name
}

# Create SQLAlchemy engine
engine = create_engine(f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Write DataFrame to PostgreSQL table using SQLAlchemy
df.to_sql('vehicle_trajectories', engine, if_exists='replace', index=False)

# Print confirmation message
print("Data loaded successfully into PostgreSQL table")
