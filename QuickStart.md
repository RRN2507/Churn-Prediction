# Quick Start Guide

Get your Churn Prediction System up and running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- pip and npm installed

## Step-by-Step Setup

### 1. Clone/Download the Project

```bash
# Create project directory
mkdir churn-prediction-project
cd churn-prediction-project
```

### 2. Backend Setup (5 steps)

```bash
# Step 1: Navigate to backend
cd backend

# Step 2: Create virtual environment
python -m venv venv

# Step 3: Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Create necessary directories
mkdir -p data/raw data/processed models
```

### 3. Add Your Data

```bash
# Copy your churnRushi.csv file to:
# backend/data/raw/churnRushi.csv
```

### 4. Train the Model

```bash
# From backend directory with venv activated:
python models/train_model.py
```

**Expected output:**
```
Starting model training pipeline...
Loading and preprocessing data...
Creating features...
Training and evaluating models...
✅ Training completed successfully!
```

### 5. Start the Backend Server

```bash
# From backend directory:
python app.py
```

**Expected output:**
```
✅ Churn Predictor initialized successfully
 * Running on http://0.0.0.0:5000
```

**Keep this terminal open!**

### 6. Frontend Setup (New Terminal)

```bash
# Open a new terminal
cd churn-prediction-project/frontend

# Install dependencies
npm install

# Start the React app
npm start
```

**Expected output:**
```
Compiled successfully!
Local:            http://localhost:3000
```

### 7. Open the Application

Your browser should automatically open to `http://localhost:3000`

If not, manually open: **http://localhost:3000**

## Testing the Application

### Quick Test with Sample Data

1. Click "Get Started" on the landing page
2. Fill in the form with these test values:
   - **Tenure**: 12 months
   - **Monthly Charges**: 85
   - **Total Charges**: 1020
   - Keep other defaults as is
3. Click "Predict Churn"

You should see a prediction result with probability!

## Troubleshooting

### Problem: "Model not found" error

**Solution:**
```bash
cd backend
python models/train_model.py
```

### Problem: Port 5000 already in use

**Solution 1:** Kill the process using port 5000
```bash
# On Mac/Linux:
lsof -ti:5000 | xargs kill -9

# On Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Solution 2:** Change the port
```bash
# Edit backend/config.py
API_PORT = 5001  # Change to any available port

# Update frontend/src/services/api.js
const API_BASE_URL = 'http://localhost:5001';
```

### Problem: CORS errors

**Solution:**
```bash
# Edit backend/config.py
CORS_ORIGINS = ['http://localhost:3000', 'http://localhost:3001']
```

### Problem: Module not found

**Solution:**
```bash
# Make sure virtual environment is activated
cd backend
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Problem: npm install fails

**Solution:**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

## Verify Installation

### Check Backend:

```bash
# Test health endpoint
curl http://localhost:5000/api/health

# Expected response:
{"status":"healthy","model_loaded":true}
```

### Check Frontend:

Open http://localhost:3000 in your browser. You should see the landing page.

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Explore the API endpoints with Postman or curl
- Customize the UI in `frontend/src/components/`
- Modify model parameters in `backend/models/train_model.py`
- Add new features in `backend/src/feature_engineering.py`

## File Checklist

Make sure you have these key files:

**Backend:**
- ✅ `backend/requirements.txt`
- ✅ `backend/config.py`
- ✅ `backend/app.py`
- ✅ `backend/models/train_model.py`
- ✅ `backend/src/data_preprocessing.py`
- ✅ `backend/src/feature_engineering.py`
- ✅ `backend/src/predict.py`
- ✅ `backend/data/raw/churnRushi.csv` (your data)

**Frontend:**
- ✅ `frontend/package.json`
- ✅ `frontend/src/App.jsx`
- ✅ `frontend/src/components/LandingPage.jsx`
- ✅ `frontend/src/components/PredictionForm.jsx`
- ✅ `frontend/src/components/ResultDisplay.jsx`
- ✅ `frontend/src/services/api.js`

## Success Indicators

You've successfully set up the project when:

1. ✅ Backend runs without errors on port 5000
2. ✅ Frontend runs without errors on port 3000
3. ✅ Landing page displays correctly
4. ✅ Prediction form accepts input
5. ✅ Predictions return results with probabilities
6. ✅ No console errors in browser

## Common Commands Reference

### Backend Commands
```bash
# Activate environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Run server
python app.py

# Train model
python models/train_model.py

# Test predictor
python src/predict.py

# Install new package
pip install package_name
pip freeze > requirements.txt
```

### Frontend Commands
```bash
# Start development server
npm start

# Build for production
npm run build

# Install new package
npm install package_name

# Run tests
npm test
```

## Production Deployment Tips

### Backend (Flask)
```bash
# Use gunicorn for production
pip install gunicorn
gunicorn app:app --bind 0.0.0.0:5000 --workers 4
```

### Frontend (React)
```bash
# Build optimized production bundle
npm run build

# Serve the build folder with a web server
```

## Need Help?

- Check the full README.md for detailed documentation
- Review error logs in terminal
- Verify all dependencies are installed
- Ensure Python and Node versions are compatible
- Check that all required files exist

---

**Happy Predicting! 🚀**