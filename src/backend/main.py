"""
Smart Financial Twin - FastAPI Backend

Endpoints:
- /predict/loan_eligibility
- /predict/fraud_risk
- /simulate/scenario
- /query (LLM integration)
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import redis
import json
from datetime import datetime
from typing import Optional, Dict, Any

# Initialize FastAPI
app = FastAPI(title="Smart Financial Twin", version="1.0.0")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Redis Client
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)

# Mock ML Models (replace with actual models in production)
def mock_loan_prediction(user_data, transactions):
    """Mock loan eligibility prediction."""
    credit_score = user_data.get("credit_score", 700)
    income = user_data.get("income", 80000)
    
    # Simplified logic
    score = min(1.0, (credit_score / 850) * 0.7 + (income / 100000) * 0.3)
    return {
        "score": round(score, 2),
        "factors": {
            "credit_score": 0.5,
            "income": 0.3,
            "savings": 0.2
        }
    }

def mock_fraud_prediction(transaction):
    """Mock fraud risk prediction."""
    amount = transaction.get("amount", 1000)
    
    # Simplified logic
    risk = "high" if amount > 50000 else "low"
    return {
        "risk": risk,
        "confidence": 0.9 if risk == "high" else 0.8
    }

# --- Models ---
class UserProfile(BaseModel):
    user_id: str
    age: int
    income: float
    credit_score: int
    employment_status: str
    savings: float

class Transaction(BaseModel):
    transaction_id: str
    user_id: str
    amount: float
    timestamp: datetime
    merchant: str
    category: str
    is_fraud: Optional[bool] = False

class LoanPredictionRequest(BaseModel):
    user_id: str
    loan_amount: float

class FraudPredictionRequest(BaseModel):
    user_id: str
    transaction_id: str

class ScenarioRequest(BaseModel):
    user_id: str
    scenario: str  # e.g., "buy a car", "lose job"

class QueryRequest(BaseModel):
    user_id: str
    query: str  # e.g., "What if my salary increases by 20%?"

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Smart Financial Twin API"}

@app.post("/predict/loan_eligibility")
def predict_loan_eligibility(request: LoanPredictionRequest):
    """Predict loan approval probability using XGBoost."""
    try:
        cache_key = f"loan_eligibility:{request.user_id}"
        cached_result = redis_client.get(cache_key)
        
        if cached_result:
            return json.loads(cached_result)
        
        # Fetch user data (mock: replace with database query)
        # In a real app, fetch from PostgreSQL:
        # user = db.query(DBUser).filter(DBUser.user_id == request.user_id).first()
        # transactions = db.query(DBTransaction).filter(DBTransaction.user_id == request.user_id).all()
        
        # Mock data (replace with actual DB query)
        user_data = {
            "user_id": request.user_id,
            "age": 30,
            "income": 80000,
            "credit_score": 720,
            "employment_status": "employed",
            "savings": 50000
        }
        
        # Mock transactions (replace with actual DB query)
        transactions = [
            {"amount": 1000, "category": "groceries", "merchant": "DMart"},
            {"amount": 2000, "category": "utilities", "merchant": "BSES"},
            {"amount": 500, "category": "entertainment", "merchant": "Netflix"}
        ]
        
        # Feature engineering
        avg_tx_amount = np.mean([tx["amount"] for tx in transactions])
        total_spend = np.sum([tx["amount"] for tx in transactions])
        tx_count = len(transactions)
        fraud_count = 0  # Assume no fraud for simplicity
        
        # Prepare features for model
        features = pd.DataFrame([{
            "credit_score": user_data["credit_score"],
            "income": user_data["income"],
            "age": user_data["age"],
            "savings": user_data["savings"],
            "avg_tx_amount": avg_tx_amount,
            "total_spend": total_spend,
            "tx_count": tx_count,
            "fraud_count": fraud_count
        }])
        
        # Mock prediction
        prediction = mock_loan_prediction(user_data, transactions)
        
        redis_client.setex(cache_key, 3600, json.dumps(prediction))
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/fraud_risk")
def predict_fraud_risk(request: FraudPredictionRequest):
    """Assess fraud risk for a transaction using CatBoost."""
    try:
        cache_key = f"fraud_risk:{request.transaction_id}"
        cached_result = redis_client.get(cache_key)
        
        if cached_result:
            return json.loads(cached_result)
        
        # Mock transaction data (replace with DB query)
        transaction = {
            "amount": 5000,
            "timestamp": "2026-07-01T12:00:00",
            "category": "shopping",
            "merchant": "Amazon"
        }
        
        # Feature engineering
        hour_of_day = pd.to_datetime(transaction["timestamp"]).hour
        amount_zscore = (transaction["amount"] - 1000) / 500  # Mock z-score
        
        # One-hot encode categorical features
        features = {
            "amount": transaction["amount"],
            "hour_of_day": hour_of_day,
            "amount_zscore": amount_zscore
        }
        
        # Add one-hot encoded features
        for cat in ["groceries", "utilities", "entertainment", "travel", "healthcare", "education", "dining", "shopping"]:
            features[f"category_{cat}"] = 1 if cat == transaction["category"] else 0
        
        for merchant in ["BigBasket", "DMart", "Reliance Fresh", "Amazon Pantry", "BSES", "Tata Power", "Mahanagar Gas", "BSNL", "BookMyShow", "Netflix", "Amazon Prime", "Spotify", "MakeMyTrip", "IRCTC", "Uber", "Ola", "Apollo Pharmacy", "Max Healthcare", "Fortis", "BYJU'S", "Unacademy", "Coursera", "Zomato", "Swiggy", "Dominos", "McDonald's", "Amazon", "Flipkart", "Myntra", "Ajio"]:
            features[f"merchant_{merchant}"] = 1 if merchant == transaction["merchant"] else 0
        
        # Prepare features for model
        features_df = pd.DataFrame([features])
        
        # Mock prediction
        prediction = mock_fraud_prediction(transaction)
        
        prediction = {
            "risk": risk,
            "confidence": float(proba),
            "factors": {
                "transaction_amount": 0.5,
                "merchant_category": 0.3,
                "time_of_day": 0.2
            }
        }
        
        redis_client.setex(cache_key, 3600, json.dumps(prediction))
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/simulate/scenario")
def simulate_scenario(request: ScenarioRequest):
    """Simulate financial scenario (e.g., "buy a car")."""
    try:
        # TODO: Replace with actual scenario simulation logic
        cache_key = f"scenario:{request.user_id}:{request.scenario}"
        cached_result = redis_client.get(cache_key)
        
        if cached_result:
            return json.loads(cached_result)
        
        # Mock simulation
        simulation = {
            "cash_flow_impact": {"month_1": -20000, "month_2": -15000},
            "loan_eligibility_drop": 0.1,
            "fraud_risk_increase": 0.05,
            "retirement_delay": 1
        }
        
        redis_client.setex(cache_key, 3600, json.dumps(simulation))
        return simulation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
def handle_query(request: QueryRequest):
    """Handle natural language queries using LLM."""
    try:
        # TODO: Replace with actual LLM integration (Llama 3/GPT)
        cache_key = f"query:{request.user_id}:{request.query}"
        cached_result = redis_client.get(cache_key)
        
        if cached_result:
            return json.loads(cached_result)
        
        # Mock response
        response = {
            "response": f"Based on your query '{request.query}', here's the simulation: Buying a car will reduce your savings by ₹1.5L and delay retirement by 1 year.",
            "impact": {
                "savings_impact": -150000,
                "retirement_delay": 1
            }
        }
        
        redis_client.setex(cache_key, 3600, json.dumps(response))
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))