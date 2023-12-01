import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
db_config = {
    "dbname": "lectures",
    "user": "postgres",
    "password": "admin",
    "host": "localhost"
}

# Establish connection to PostgreSQL database
engine = create_engine(f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['dbname']}")

# Base path for CSV files
base_path = "./data/"

# List of table names and corresponding CSV files
tables_and_files = {
    "students": "students.csv",
    "lecturers": "lecturers.csv",
    "rooms": "rooms.csv",
    "modules": "modules.csv",
    "courses": "courses.csv",
    "grades": "grades.csv",
    "enrollments": "enrollments.csv"
}

# Load data from CSV files into PostgreSQL tables
for table, file_name in tables_and_files.items():
    file_path = base_path + file_name

    # Load data into DataFrame
    df = pd.read_csv(file_path)

    # Load data into PostgreSQL table
    # Replace the table if it already exists
    df.to_sql(table, engine, schema='public', index=False, if_exists='append')

print("Data successfully loaded into PostgreSQL database.")
