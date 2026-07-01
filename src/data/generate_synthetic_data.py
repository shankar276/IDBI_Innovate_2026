"""
Generate synthetic banking data for Smart Financial Twin.

Outputs:
- users.csv: 1,000 user profiles (income, credit score, employment status).
- transactions.csv: 10,000 transactions (amount, merchant, category, fraud flags).
"""

import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import uuid

# Initialize Faker
fake = Faker()

# --- User Profiles ---
def generate_users(num_users=1000):
    """Generate synthetic user profiles."""
    users = []
    for _ in range(num_users):
        age = random.randint(18, 70)
        income = round(random.uniform(20000, 500000), 2)
        credit_score = random.randint(300, 850)
        employment_status = random.choice(["employed", "self_employed", "unemployed"])
        savings = round(random.uniform(0, 1000000), 2)
        
        users.append({
            "user_id": str(uuid.uuid4()),
            "age": age,
            "income": income,
            "credit_score": credit_score,
            "employment_status": employment_status,
            "savings": savings,
            "created_at": fake.date_time_this_year().isoformat()
        })
    
    return pd.DataFrame(users)

# --- Transactions ---
def generate_transactions(users_df, num_transactions=10000):
    """Generate synthetic transactions."""
    transactions = []
    categories = ["groceries", "utilities", "entertainment", "travel", "healthcare", "education", "dining", "shopping"]
    merchants = {
        "groceries": ["BigBasket", "DMart", "Reliance Fresh", "Amazon Pantry"],
        "utilities": ["BSES", "Tata Power", "Mahanagar Gas", "BSNL"],
        "entertainment": ["BookMyShow", "Netflix", "Amazon Prime", "Spotify"],
        "travel": ["MakeMyTrip", "IRCTC", "Uber", "Ola"],
        "healthcare": ["Apollo Pharmacy", "Max Healthcare", "Fortis"],
        "education": ["BYJU'S", "Unacademy", "Coursera"],
        "dining": ["Zomato", "Swiggy", "Dominos", "McDonald's"],
        "shopping": ["Amazon", "Flipkart", "Myntra", "Ajio"]
    }
    
    for _ in range(num_transactions):
        user = users_df.sample(1).iloc[0]
        category = random.choice(categories)
        merchant = random.choice(merchants[category])
        amount = round(random.uniform(100, 100000), 2)
        
        # Fraud probability: 2% of transactions
        is_fraud = random.choices([True, False], weights=[0.02, 0.98])[0]
        
        # Adjust fraud likelihood based on user profile
        if user["credit_score"] < 500:
            is_fraud = random.choices([True, False], weights=[0.1, 0.9])[0]
        
        transactions.append({
            "transaction_id": str(uuid.uuid4()),
            "user_id": user["user_id"],
            "amount": amount,
            "timestamp": fake.date_time_this_year().isoformat(),
            "merchant": merchant,
            "category": category,
            "is_fraud": is_fraud
        })
    
    return pd.DataFrame(transactions)

# --- Main ---
if __name__ == "__main__":
    print("Generating synthetic data...")
    
    # Generate users
    users_df = generate_users(1000)
    users_df.to_csv("raw/users.csv", index=False)
    print("[OK] Generated users.csv (1,000 users)")
    
    # Generate transactions
    transactions_df = generate_transactions(users_df, 10000)
    transactions_df.to_csv("raw/transactions.csv", index=False)
    print("[OK] Generated transactions.csv (10,000 transactions)")
    
    print("\nSample User Data:")
    print(users_df.head())
    
    print("\nSample Transaction Data:")
    print(transactions_df.head())
    
    print("\nFraudulent Transactions:")
    print(transactions_df[transactions_df["is_fraud"]].head())