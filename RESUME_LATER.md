# 🔄 Resume Later: Smart Financial Twin

## 📌 **Completed Tasks**
### **1. Backend (FastAPI)**
- ✅ **Initialized FastAPI Project** with:
  - Loan eligibility, fraud risk, and scenario simulation APIs.
  - Redis caching for real-time predictions.
- ✅ **Database Setup** (PostgreSQL schema ready; synthetic data generated).
- **API Endpoints**
  | Endpoint | Method | Description | Input | Output |
  |----------|--------|-------------|-------|--------|
  | `/predict/loan_eligibility` | POST | Predict loan approval probability | `{user_id: str, loan_amount: float}` | `{score: float, factors: dict}` |
  | `/predict/fraud_risk` | POST | Assess fraud risk for a transaction | `{user_id: str, transaction_id: str}` | `{risk: str, confidence: float}` |
  | `/simulate/scenario` | POST | Simulate financial scenario | `{user_id: str, scenario: str}` | `{impact: dict}` |

---

### **2. Synthetic Data Generation**
- **Tools**: `faker`, `pandas`, `numpy`.
- **Data Schema**:
  ```python
  # Users
  {
    "user_id": str,
    "age": int,
    "income": float,
    "credit_score": int,
    "employment_status": str,
    "savings": float
  }

  # Transactions
  {
    "transaction_id": str,
    "user_id": str,
    "amount": float,
    "timestamp": datetime,
    "merchant": str,
    "category": str,
    "is_fraud": bool
  }
  ```
- **Script**: `src/data/generate_synthetic_data.py`.

---

### **3. ML Models**
- **Loan Eligibility (XGBoost)**
  - **Features**: Credit score, income, debt-to-income ratio, employment history.
  - **Target**: Probability of loan approval.
- **Fraud Detection (CatBoost)**
  - **Features**: Transaction amount, merchant category, time since last transaction.
  - **Target**: Binary fraud label.
- **Cash Flow Forecasting (LightGBM)**
  - **Features**: Historical transactions, income stability, seasonal trends.
  - **Target**: Next 3 months' cash flow.
- **Explainability (SHAP)**
  - Generate feature importance plots for all models.

---

## 📌 **Post-Submission Roadmap**
### **1. LLM Integration (Llama 3/GPT)**
- **Status**: Mock API implemented (`/query` endpoint).
- **Next Steps**: Replace with actual LLM (e.g., Llama 3 or GPT-4).
- **Example**:
  ```python
  @app.post("/query")
  def handle_query(query: str, user_id: str):
      scenario = parse_query(query)  # e.g., "buy a car" → {action: "purchase", item: "car", amount: 1500000}
      impact = simulate_scenario(user_id, scenario)
      return {"response": f"Buying a car will reduce your savings by ₹{impact['savings_impact']} and delay retirement by {impact['retirement_delay']} years."}
  ```

---

### **5. Scenario Simulation Engine**
- **Inputs**: User query (e.g., "What if I lose my job?").
- **Logic**:
  1. Adjust income/expenses based on scenario.
  2. Re-run ML models (loan eligibility, fraud risk).
  3. Generate visual impact report (Plotly).
- **Output**: JSON with:
  ```json
  {
    "cash_flow_impact": {"month_1": -20000, "month_2": -15000},
    "loan_eligibility_drop": 0.3,
    "fraud_risk_increase": 0.15,
    "retirement_delay": 2
  }
  ```

---

## 📌 **Current Status (Jul 08, 2026)**

### **✅ FULLY WORKING - Local Deployment**
- **Frontend**: http://localhost:5173 — Dashboard + Scenario Simulator **fully functional**
- **Backend**: http://localhost:8000/docs — All API endpoints return valid JSON
- **Scenario Simulator**: ✅ Returns cash flow impact, loan eligibility drop, fraud risk increase, retirement delay
- Docker (PostgreSQL + Redis) running locally

### **⚠️ PARTIAL - AWS EC2 Deployment**
- **Instance**: t2.micro (12GB EBS) — Ubuntu 22.04
- **Public IP**: 54.158.246.103
- **Backend**: http://54.158.246.103:8000/docs — ✅ **Working** (verified via curl)
- **Frontend**: http://54.158.246.103:5173 — ⚠️ **Loads but Scenario Simulator FAILS** ("Failed to simulate scenario")
- **Root Cause**: Likely CORS or API URL mismatch in production build (hardcoded localhost vs public IP)

---

## 📌 **Pending Tasks (Critical Priority)**
### **1. Fix AWS Frontend Scenario Simulator (CRITICAL)**
- Check browser console (F12) for exact error
- Verify API URL in production build points to `http://54.158.246.103:8000` (NOT localhost)
- Verify FastAPI CORS allows `http://54.158.246.103:5173`
- Rebuild frontend with correct API URL and redeploy

### **2. Demo Visuals (for Submission)**
- **Dashboard Screenshot**: Capture `http://localhost:5173` → `demo/screenshots/dashboard.png`.
- **API Logs Screenshot**: Test `/predict/loan_eligibility` → `demo/screenshots/api_logs.png`.
- **Pitch Deck GIF**: Convert `slides.pptx` → `demo/pitch_deck.gif`.
- **Backup Video**: Record 5-minute demo → `demo/video/demo_recording.mp4`.

### **3. Documentation & Submission**
- **5-Page PDF (`docs/submission.pdf`)**: Compile `SESSION_SUMMARY.md` + screenshots.
- **Final GitHub Push**: Sync all changes before 15 July 2026.

---

## 🔍 **Blockers & Notes**
1. **AWS Frontend Issue**: Simulator fails — likely CORS or API URL mismatch in production build.
2. **Deployment**: FastAPI + React integration (CORS, environment variables) needs verification on AWS.
3. **EBS Volume**: Expanded from 8GB→12GB for ML library installation.

---

## 📅 **Timeline (Hackathon Deadline: 15 July 2026)**
| Task | Deadline | Status |
|------|----------|--------|
| **Fix AWS frontend scenario simulator** | **ASAP** | 🔄 **IN PROGRESS** |
| Demo Visuals (screenshots, GIF, video) | 5 July | ✅ Done (local) |
| 5-Page PDF (docs/submission.pdf) | 8 July | 🔄 In Progress |
| Final GitHub Push | 14 July | 🔄 Pending |