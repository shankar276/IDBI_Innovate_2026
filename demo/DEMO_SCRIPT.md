# 🎬 Smart Financial Twin - Demo Script
**IDBI InnovaTech 2026 Submission**

This script guides you through a **5-minute live demo** of the **Smart Financial Twin** project.

---

## 📌 **Demo Flow**
| Time  | Action | Script | Visuals |
|-------|--------|--------|---------|
| **0:00 - 0:30** | **Introduction** | "Meet Smart Financial Twin—your AI-powered personal finance advisor. Today, I’ll show how it predicts loan eligibility, detects fraud, and simulates financial scenarios." | ![Slide 1: Title Slide](https://via.placeholder.com/800x450/0078d4/ffffff?text=Smart+Financial+Twin)
| **0:30 - 1:30** | **User Login & Dashboard Overview** | "Let’s log in as a mock user. The dashboard shows:
1. **Financial Health Score** (85/100).
2. **Cash Flow Forecast** (next 6 months).
3. **Fraud Risk Assessment** (low/medium/high)." | ![Dashboard](https://via.placeholder.com/800x450/1e293b/ffffff?text=Dashboard+Overview)
| **1:30 - 2:30** | **Loan Eligibility Prediction** | "Can this user afford a ₹5L home loan? The AI analyzes:
- Credit score (720).
- Income (₹80K/month).
- Savings (₹50K).
**Result**: 85% approval probability!" | ![Loan Eligibility](https://via.placeholder.com/400x300/3b82f6/ffffff?text=Loan+Eligibility:+85%25)
| **2:30 - 3:30** | **Fraud Risk Detection** | "Let’s check a ₹5K transaction. The AI flags:
- **Merchant**: Amazon (high-risk category).
- **Amount**: ₹5K (unusual for this user).
**Result**: Medium risk (75% confidence)." | ![Fraud Risk](https://via.placeholder.com/400x300/ef4444/ffffff?text=Fraud+Risk:+Medium)
| **3:30 - 4:30** | **Scenario Simulation** | "What if the user buys a ₹15L car? The AI simulates:
- **Savings Impact**: -₹1.5L.
- **Retirement Delay**: +1 year.
- **Loan Eligibility Drop**: 20%." | ![Scenario Simulation](https://via.placeholder.com/400x300/10b981/ffffff?text=Scenario:+Buy+a+Car)
| **4:30 - 5:00** | **Conclusion & Q&A** | "Smart Financial Twin helps users make smarter financial decisions with AI. Thank you!" | ![Slide 5: Business Impact](https://via.placeholder.com/800x450/f59e0b/ffffff?text=Business+Impact:+30%25+Fewer+Defaults)

---

## 🎥 **Demo Visuals**
### **1. Dashboard Screenshot**
- **File**: `demo/screenshots/dashboard.png` (save a screenshot of `http://localhost:5173`).
- **How to Capture**:
  ```bash
  # On Windows (using PowerShell)
  Add-Type -AssemblyName System.Windows.Forms
  $screen = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
  $bitmap = New-Object System.Drawing.Bitmap($screen.Width, $screen.Height)
  $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
  $graphics.CopyFromScreen(0, 0, 0, 0, $bitmap.Size)
  $bitmap.Save("demo/screenshots/dashboard.png")
  ```

### **2. API Request/Response Logs**
- **File**: `demo/api_logs.md`
- **Example**:
  ```markdown
  ### Loan Eligibility API
  **Request**:
  ```json
  POST /predict/loan_eligibility
  {
    "user_id": "mock_user_123",
    "loan_amount": 500000
  }
  ```
  
  **Response**:
  ```json
  {
    "score": 0.85,
    "factors": {
      "credit_score": 0.5,
      "income": 0.3,
      "savings": 0.2
    }
  }
  ```
  ```

### **3. Pitch Deck GIF**
- **File**: `demo/pitch_deck.gif`
- **How to Create**:
  ```bash
  # Install ffmpeg (Linux/macOS)
  sudo apt install ffmpeg  # Ubuntu/Debian
  brew install ffmpeg      # macOS
  
  # Convert slides.pptx to GIF (using PowerPoint or online tools)
  # Or record a screen capture:
  ffmpeg -f gdigrab -framerate 30 -i desktop demo/pitch_deck.gif
  ```

---

## 🛠️ **Demo Setup Checklist**
| Task | Status |
|------|--------|
| [ ] Start FastAPI backend (`uvicorn main:app --reload`) | ⬜ |
| [ ] Start React frontend (`npm run dev`) | ⬜ |
| [ ] Open dashboard (`http://localhost:5173`) | ⬜ |
| [ ] Test API endpoints (`http://localhost:8000/docs`) | ⬜ |
| [ ] Capture screenshots (dashboard, API logs) | ⬜ |
| [ ] Generate pitch deck GIF | ⬜ |

---

## 🎤 **Pro Tips for Live Demo**
1. **Preload Data**: Use mock data to avoid real-time delays.
2. **Practice Timing**: Stick to **5 minutes** (use a timer).
3. **Highlight Innovation**: Emphasize **AI explainability** (SHAP) and **scenario simulation**.
4. **Engage Judges**: Ask, "What scenario would you like to simulate?"
5. **Backup Plan**: Record a **video demo** in case of technical issues.

---

## 📁 **Demo Folder Structure**
```
demo/
├── DEMO_SCRIPT.md          # This file
├── screenshots/
│   ├── dashboard.png        # Dashboard screenshot
│   └── api_logs.png         # API request/response
├── pitch_deck.gif          # Animated pitch deck
└── video/
    └── demo_recording.mp4   # Backup video demo
```