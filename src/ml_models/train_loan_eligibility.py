"""
Train XGBoost model for loan eligibility prediction.

Input: users.csv + transactions.csv (synthetic data).
Output: Trained model (loan_eligibility_xgboost.json) + SHAP explainability.
"""

import pandas as pd
import numpy as np
import xgboost as xgb
import shap
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
import os

# --- Load Data ---
def load_data():
    """Load and preprocess data."""
    users_df = pd.read_csv("../data/raw/users.csv")
    transactions_df = pd.read_csv("../data/raw/transactions.csv")
    
    # Feature Engineering: Aggregate transactions
    user_transactions = transactions_df.groupby("user_id").agg({
        "amount": ["mean", "sum", "count"],
        "is_fraud": "sum"
    })
    user_transactions.columns = ["avg_tx_amount", "total_spend", "tx_count", "fraud_count"]
    
    # Merge with user profiles
    data = pd.merge(users_df, user_transactions, on="user_id", how="left")
    data.fillna(0, inplace=True)
    
    # Target: Loan Eligibility (simplified: credit_score > 650 and income > 50000)
    data["loan_eligible"] = ((data["credit_score"] > 650) & (data["income"] > 50000)).astype(int)
    
    return data

# --- Train Model ---
def train_model(data):
    """Train XGBoost model."""
    # Features
    features = [
        "credit_score", "income", "age", "savings",
        "avg_tx_amount", "total_spend", "tx_count", "fraud_count"
    ]
    X = data[features]
    y = data["loan_eligible"]
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train XGBoost
    model = xgb.XGBClassifier(
        objective="binary:logistic",
        eval_metric="logloss",
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1
    )
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"ROC AUC: {roc_auc_score(y_test, y_pred_proba):.4f}")
    
    return model, X_train

# --- Explainability ---
def explain_model(model, X_train):
    """Generate SHAP explainability."""
    explainer = shap.Explainer(model)
    shap_values = explainer(X_train)
    
    # Save SHAP summary plot
    shap.summary_plot(shap_values, X_train, show=False)
    shap.savefig("loan_eligibility_shap.png")
    print("✅ SHAP explainability plot saved: loan_eligibility_shap.png")

# --- Main ---
if __name__ == "__main__":
    print("Training loan eligibility model...")
    
    # Load data
    data = load_data()
    
    # Train model
    model, X_train = train_model(data)
    
    # Save model
    joblib.dump(model, "loan_eligibility_xgboost.joblib")
    print("[OK] Model saved: loan_eligibility_xgboost.joblib")
    
    # Explainability
    explain_model(model, X_train)