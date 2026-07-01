# 🚀 Deployment Guide: Smart Financial Twin

This guide explains how to deploy **Smart Financial Twin** on a fresh server (Ubuntu 22.04 LTS).

---

## 📋 **Prerequisites**
1. **Server**: Ubuntu 22.04 LTS (or any Linux distro).
2. **Hardware**: 4GB+ RAM, 2+ CPU cores.
3. **Software**:
   - Docker (for PostgreSQL/Redis)
   - Python 3.10+
   - Node.js 18+
   - Git

---

## 🔧 **Step 1: Clone the Repository**
```bash
# Clone the repo
git clone https://github.com/shankar276/IDBI_Innovate_2026.git
cd IDBI_Innovate_2026/repo

# Set up environment variables
cp .env.example .env  # Update .env with your credentials
```

---

## 🐳 **Step 2: Start PostgreSQL & Redis (Docker)**
```bash
# Start PostgreSQL
docker run --name smart-financial-twin-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=smart_financial_twin \
  -p 5432:5432 \
  -d postgres:15

# Start Redis
docker run --name smart-financial-twin-redis \
  -p 6379:6379 \
  -d redis:7
```

---

## 🐍 **Step 3: Set Up Backend (FastAPI)**
```bash
# Navigate to backend
cd src/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Import synthetic data into PostgreSQL
python ../../src/data/import_data_to_postgres.py

# Start FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🌐 **Step 4: Set Up Frontend (React)**
```bash
# Navigate to frontend
cd ../frontend

# Install dependencies
npm install

# Start React app
npm run dev
```

---

## 🔐 **Step 5: Configure Nginx (Production)**
1. **Install Nginx**:
   ```bash
   sudo apt update && sudo apt install nginx -y
   ```

2. **Configure Nginx** (`/etc/nginx/sites-available/smart-financial-twin`):
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:5173;
           proxy_set_header Host $host;
       }

       location /api {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
       }
   }
   ```

3. **Enable the config**:
   ```bash
   sudo ln -s /etc/nginx/sites-available/smart-financial-twin /etc/nginx/sites-enabled/
   sudo nginx -t && sudo systemctl restart nginx
   ```

---

## 🛡️ **Step 6: Secure with HTTPS (Let's Encrypt)**
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtain SSL certificate
sudo certbot --nginx -d your-domain.com
```

---

## 📊 **Step 7: Monitor & Scale**
1. **PM2 (Process Manager)**:
   ```bash
   npm install -g pm2
   pm2 start "npm run dev" --name frontend
   pm2 start "uvicorn main:app --host 0.0.0.0 --port 8000" --name backend
   pm2 save && pm2 startup
   ```

2. **Docker Compose (Optional)**:
   ```yaml
   # docker-compose.yml
   version: "3.8"
   services:
     postgres:
       image: postgres:15
       environment:
         POSTGRES_USER: postgres
         POSTGRES_PASSWORD: postgres
         POSTGRES_DB: smart_financial_twin
       ports:
         - "5432:5432"
       volumes:
         - postgres_data:/var/lib/postgresql/data
     
     redis:
       image: redis:7
       ports:
         - "6379:6379"
     
     backend:
       build: ./src/backend
       ports:
         - "8000:8000"
       depends_on:
         - postgres
         - redis
     
     frontend:
       build: ./src/frontend
       ports:
         - "5173:5173"
       depends_on:
         - backend
   
   volumes:
     postgres_data:
   ```

---

## 🧪 **Step 8: Test the Deployment**
1. **Frontend**: [http://your-domain.com](http://your-domain.com)
2. **Backend API**: [http://your-domain.com/api/docs](http://your-domain.com/api/docs)
3. **PostgreSQL**: `psql -h localhost -U postgres -d smart_financial_twin`
4. **Redis**: `redis-cli ping` (should return `PONG`)

---

## 🐞 **Troubleshooting**
| Issue | Solution |
|-------|----------|
| **PostgreSQL connection refused** | Check if Docker container is running: `docker ps` |
| **FastAPI CORS errors** | Ensure `CORSMiddleware` is configured in `main.py` |
| **React app not loading** | Verify `npm run dev` is running and ports are open |
| **ML model errors** | Check if models are in `src/backend/` and paths are correct |

---

## 📅 **Post-Deployment Checklist**
- [ ] Set up **CI/CD** (GitHub Actions/GitLab CI).
- [ ] Configure **logging** (ELK Stack or Prometheus + Grafana).
- [ ] Enable **auto-scaling** (Kubernetes or AWS ECS).
- [ ] Replace mock ML models with **production-ready models**.
- [ ] Integrate **real banking APIs** (IDBI Sandbox).