"""
Import synthetic data into PostgreSQL for Smart Financial Twin.

Requires:
- PostgreSQL running locally (host: localhost, port: 5432, user: postgres, password: postgres).
- Tables created via `database.py` (users, transactions).
"""

import pandas as pd
from sqlalchemy import create_engine
import os

# PostgreSQL Configuration
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5432"
POSTGRES_DB = "smart_financial_twin"

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL)

# --- Import Functions ---
def import_users():
    """Import users.csv into PostgreSQL."""
    users_df = pd.read_csv("raw/users.csv")
    users_df.to_sql(
        "users",
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )
    print(f"✅ Imported {len(users_df)} users into PostgreSQL.")

def import_transactions():
    """Import transactions.csv into PostgreSQL."""
    transactions_df = pd.read_csv("raw/transactions.csv")
    transactions_df.to_sql(
        "transactions",
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )
    print(f"✅ Imported {len(transactions_df)} transactions into PostgreSQL.")

# --- Main ---
if __name__ == "__main__":
    print("Importing data to PostgreSQL...")
    
    try:
        import_users()
        import_transactions()
        print("\n🎉 Data import completed successfully!")
    except Exception as e:
        print(f"❌ Error importing data: {e}")
        print("\nTroubleshooting:")
        print("- Ensure PostgreSQL is running locally (host: localhost, port: 5432).")
        print("- Verify database 'smart_financial_twin' exists.")
        print("- Check tables 'users' and 'transactions' are created (run database.py).")