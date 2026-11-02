import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# I add this script so works from any folder:
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
load_dotenv(BASE_DIR / ".env")

# Database connection configuration
USERNAME = 'postgres'
PASSWORD = os.getenv("DB_PASSWORD")
HOST = 'localhost'
PORT = '5432'
DATABASE = 'critical_eye_db'

connection_string = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(connection_string)
print("Database engine configured successfully!")

# --- ISOT dataset (True.csv and Fake.csv) ---
try:
    print("\nLoading ISOT datasets from CSV...")
    true_df = pd.read_csv(DATA_DIR / "True.csv")
    fake_df = pd.read_csv(DATA_DIR / "Fake.csv")

    # Tracking label: 0 = real news, 1 = fake news
    true_df['is_fake'] = 0
    fake_df['is_fake'] = 1

    isot_combined = pd.concat([true_df, fake_df], ignore_index=True)
    # Replace the table if it exists, inserting rows in batches of 1,000
    isot_combined.to_sql('isot_raw', con=engine, if_exists='replace', index=False, chunksize=1000)
    print("ISOT dataset successfully loaded into the database!")

except Exception as e:
    print(f"Error loading ISOT dataset: {e}")

# --- WELFake dataset (WELFake_Dataset.csv) ---
try:
    print("\nLoading WELFake dataset from CSV...")
    welfake_df = pd.read_csv(DATA_DIR / "WELFake_Dataset.csv")

    # Rename the first column to 'id' so it matches the SQL table column name
    welfake_df.rename(columns={welfake_df.columns[0]: 'id'}, inplace=True)

    print(f"Pushing {len(welfake_df):,} records to 'welfake_raw' table in PostgreSQL...")
    welfake_df.to_sql('welfake_raw', con=engine, if_exists='replace', index=False, chunksize=1000)
    print("WELFake dataset successfully loaded into the database!")
    print("\nALL DATASETS IMPORTED SUCCESSFULLY!")

except Exception as e:
    print(f"Error loading WELFake dataset: {e}")