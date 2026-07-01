"""
Train CatBoost model for fraud detection.

Input: transactions.csv (synthetic data).
Output: Trained model (fraud_detection_catboost.cbm) + SHAP explainability.
"""

import pandas as pd
import numpy as np
from catboost import CatBoostClassifier, Pool
import shap
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score

# --- Load Data ---
def load_data():
    """Load and preprocess transactions data."""
    transactions_df = pd.read_csv("../data/raw/transactions.csv")
    
    # Feature Engineering
    transactions_df["hour_of_day"] = pd.to_datetime(transactions_df["timestamp"]).dt.hour
    transactions_df["amount_zscore"] = (transactions_df["amount"] - transactions_df["amount"].mean()) / transactions_df["amount"].std()
    
    # Encode categorical variables
    transactions_df = pd.get_dummies(transactions_df, columns=["category", "merchant"])
    
    return transactions_df

# --- Train Model ---
def train_model(data):
    """Train CatBoost model."""
    # Features
    features = [
        "amount", "hour_of_day", "amount_zscore"
    ] + [col for col in data.columns if col.startswith("category_") or col.startswith("merchant_")]
    
    X = data[features]
    y = data["is_fraud"]
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train CatBoost
    model = CatBoostClassifier(
        iterations=100,
        depth=6,
        learning_rate=0.1,
        loss_function="Logloss",
        eval_metric="AUC",
        verbose=10
    )
    model.fit(X_train, y_train, eval_set=(X_test, y_test))
    
    # Evaluate
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print(f"ROC AUC: {roc_auc_score(y_test, y_pred_proba):.4f}")
    
    return model, X_train

# --- Explainability ---
def explain_model(model, X_train):
    """Generate SHAP explainability."""
    explainer = shap.Explainer(model)
    shap_values = explainer(X_train)
    
    # Save SHAP summary plot
    shap.summary_plot(shap_values, X_train, show=False)
    shap.savefig("fraud_detection_shap.png")
    print("✅ SHAP explainability plot saved: fraud_detection_shap.png")

# --- Main ---
if __name__ == "__main__":
    print("Training fraud detection model...")
    
    # Load data
    data = load_data()
    
    # Train model
    model, X_train = train_model(data)
    
    # Save model
    model.save_model("fraud_detection_catboost.cbm")
    print("[OK] Model saved: fraud_detection_catboost.cbm")
    
    # Explainability
    explain_model(model, X_train)