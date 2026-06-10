import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

# Database Connection Configuration
USERNAME = 'postgres'
PASSWORD = os.getenv("DB_PASSWORD")  
HOST = 'localhost'
PORT = '5432'
DATABASE = 'critical_eye_db'

# Creating the connection engine
connection_string = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(connection_string)
print("Database engine configured successfully!")

# - Import and Process ISOT Dataset (True.csv and Fake.csv)
try:
    print("\n Loading ISOT datasets from CSV...")
    true_df = pd.read_csv("data/True.csv")
    fake_df = pd.read_csv("data/Fake.csv")
    
    # Adding tracking label: 0 for true/real news, 1 for fake news
    true_df['is_fake'] = 0
    fake_df['is_fake'] = 1
    
    # Combine them into a single dataframe
    isot_combined = pd.concat([true_df, fake_df], ignore_index=True)    
    # Append the data directly to the existing table
    isot_combined.to_sql('isot_raw', con=engine, if_exists='replace', index=False)    
    print("ISOT dataset successfully loaded into the database!")

except Exception as e:
    print(f"Error loading ISOT dataset: {e}")

# - Import and Process WELFake Dataset (WELFake_Dataset.csv)
try:
    print("\n Loading WELFake dataset from CSV...")
    welfake_df = pd.read_csv("data/WELFake_Dataset.csv")
    
    # Rename the first column to 'id' so it matches the SQL table column name perfectly
    welfake_df.rename(columns={welfake_df.columns[0]: 'id'}, inplace=True)
    
    print(f"Pushing {len(welfake_df):,} records to 'welfake_raw' table in PostgreSQL...")
    welfake_df.to_sql('welfake_raw', con=engine, if_exists='replace', index=False)    
    print("WELFake dataset successfully loaded into the database!")
    print("\nALL DATASETS IMPORTED SUCCESSFULLY!")

except Exception as e:
    print(f"Error loading WELFake dataset: {e}")