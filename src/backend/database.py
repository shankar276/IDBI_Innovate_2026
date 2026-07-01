"""
Database setup for Smart Financial Twin.

- PostgreSQL: Stores user profiles, transactions, predictions.
- Redis: Caches real-time predictions (fraud risk, loan eligibility).
"""

from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# PostgreSQL Configuration
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "smart_financial_twin")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# SQLAlchemy Setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- Database Models ---
class DBUser(Base):
    """User profile model."""
    __tablename__ = "users"
    
    user_id = Column(String, primary_key=True, index=True)
    age = Column(Integer)
    income = Column(Float)
    credit_score = Column(Integer)
    employment_status = Column(String)
    savings = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class DBTransaction(Base):
    """Transaction model."""
    __tablename__ = "transactions"
    
    transaction_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    merchant = Column(String)
    category = Column(String)
    is_fraud = Column(Boolean, default=False)

class DBPrediction(Base):
    """Prediction results model."""
    __tablename__ = "predictions"
    
    prediction_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)
    prediction_type = Column(String)  # "loan_eligibility", "fraud_risk"
    result = Column(String)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()