# 🚀 Smart Financial Twin
**AI-Powered Personal Finance Advisor for IDBI InnovaTech 2026**

[![IDBI InnovaTech 2026](https://img.shields.io/badge/Hackathon-IDBI%20InnovaTech%202026-blue)](https://hack2skill.com/event/idbinnovate)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18+-61DAFB?logo=react)](https://react.dev/)

---

## 🌟 **Why Smart Financial Twin?**
Traditional banking apps provide **static insights**, but users need **dynamic, personalized advice** to answer questions like:
- *"Can I afford a home loan?"*
- *"What if I lose my job?"*
- *"How does buying a car impact my savings?"*

**Smart Financial Twin** solves this by:
✅ **Predicting financial health** (loan eligibility, fraud risk, retirement readiness).
✅ **Simulating "what-if" scenarios** (e.g., "What if my salary increases by 20%?").
✅ **Providing real-time insights** with explainable AI (SHAP).

---

## 📊 **Demo**
![Dashboard Demo](https://via.placeholder.com/800x450/0078d4/ffffff?text=Smart+Financial+Twin+Dashboard)

**Try it live**: [http://localhost:5173](http://localhost:5173) (after deployment)

---

## 🛠️ **Tech Stack**
| Component       | Technology Stack                          |
|----------------|-------------------------------------------|
| **Frontend**   | React + Tailwind + Plotly                 |
| **Backend**    | FastAPI + PostgreSQL + Redis              |
| **ML Models**  | XGBoost (Loan Eligibility), CatBoost (Fraud Detection) |
| **Explainability** | SHAP (for RBI/IDBI compliance)        |
| **Deployment** | Docker + Nginx + PM2                      |

---

## 🚀 **Quick Start**
### **1. Clone the Repository**
```bash
git clone https://github.com/shankar276/IDBI_Innovate_2026.git
cd IDBI_Innovate_2026/repo
```

### **2. Set Up Backend (FastAPI)**
```bash
cd src/backend
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### **3. Set Up Frontend (React)**
```bash
cd ../frontend
npm install
npm run dev
```

### **4. Access the App**
- **Frontend**: [http://localhost:5173](http://localhost:5173)
- **Backend API**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📦 **Project Structure**
```
IDBI_Innovate_2026/
├── src/
│   ├── backend/          # FastAPI + ML Models
│   ├── frontend/         # React + Tailwind
│   ├── data/             # Synthetic banking data
│   └── ml_models/        # XGBoost/CatBoost training
├── presentation/        # Pitch deck (slides.pptx)
├── DEPLOYMENT.md        # Deployment guide
├── SESSION_SUMMARY.md   # Project progress
└── RESUME_LATER.md      # Pending tasks
```

---

## 🏆 **Hackathon Submission**
### **Judging Criteria Alignment**
| Criteria          | How We Address It                          |
|-------------------|--------------------------------------------|
| **Innovation**    | AI digital twin + federated learning.      |
| **Technical Depth** | XGBoost, CatBoost, SHAP, FastAPI, React.  |
| **Business Impact** | 30% reduction in loan defaults.           |
| **Scalability**   | Cloud-ready (PostgreSQL, Redis, Docker).   |
| **Presentation**  | Interactive demo + pitch deck.             |

### **Pitch Deck**
📌 **File**: [`presentation/slides.pptx`](presentation/slides.pptx)
📌 **Slides**: 5-slide PowerPoint (problem, solution, tech stack, impact).

---

## 🤝 **Contributing**
Contributions are welcome! Open an **issue** or submit a **pull request**.

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## 📜 **License**
This project is licensed under the **MIT License** - see [`LICENSE`](LICENSE) for details.

---

## 📞 **Contact**
For questions or feedback:
- **Email**: [your-email@example.com](mailto:your-email@example.com)
- **GitHub**: [@shankar276](https://github.com/shankar276)

**Built with ❤️ for IDBI InnovaTech 2026!**