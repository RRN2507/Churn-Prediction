# Customer Churn Prediction System

An end-to-end machine learning project for predicting customer churn with a React frontend and Flask backend.

## 🎯 Project Overview

This project predicts whether a customer will churn (leave the service) based on various features like demographics, services, and billing information. The system uses machine learning models trained on customer data to provide real-time predictions.

## 📁 Project Structure

```
churn-prediction-project/
├── backend/                    # Flask API backend
│   ├── app.py                 # Main Flask application
│   ├── config.py              # Configuration settings
│   ├── requirements.txt       # Python dependencies
│   ├── data/                  # Data directory
│   │   ├── raw/              # Raw data files
│   │   └── processed/        # Processed data files
│   ├── models/               # ML models directory
│   │   └── train_model.py    # Model training script
│   └── src/                  # Source code
│       ├── data_preprocessing.py
│       ├── feature_engineering.py
│       └── predict.py
│
└── frontend/                  # React frontend
    ├── public/
    ├── src/
    │   ├── App.jsx
    │   ├── components/
    │   │   ├── LandingPage.jsx
    │   │   ├── PredictionForm.jsx
    │   │   └── ResultDisplay.jsx
    │   └── services/
    │       └── api.js
    └── package.json
```

## 🚀 Setup Instructions

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Place your dataset:**
   - Copy `churnRushi.csv` to `backend/data/raw/`

5. **Train the model:**
   ```bash
   python models/train_model.py
   ```
   This will:
   - Preprocess the data
   - Train multiple ML models
   - Save the best model and preprocessing objects

6. **Run the Flask API:**
   ```bash
   python app.py
   ```
   The API will run on `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Create .env file (optional):**
   ```bash
   REACT_APP_API_URL=http://localhost:5000
   ```

4. **Start the development server:**
   ```bash
   npm start
   ```
   The app will open on `http://localhost:3000`

## 🎨 Features

### Landing Page
- Beautiful gradient design
- Feature highlights
- Statistics display
- Call-to-action button

### Prediction Form
- Comprehensive customer data input
- Organized sections (Demographics, Services, Billing)
- Form validation
- Real-time API integration

### Results Display
- Visual probability indicators
- Churn/No-churn classification
- Confidence levels
- Actionable recommendations for high-risk customers

## 📊 Model Information

The system trains and compares multiple models:
- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost

The best performing model (based on F1 score) is automatically selected and saved.

## 🔌 API Endpoints

### `GET /`
Home endpoint with API information

### `GET /api/health`
Health check endpoint

### `POST /api/predict`
Make a single prediction

**Request Body:**
```json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "No",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 85.0,
  "TotalCharges": 1020.0
}
```

**Response:**
```json
{
  "success": true,
  "prediction": {
    "churn": "Yes",
    "churn_probability": 0.85,
    "no_churn_probability": 0.15,
    "confidence": 0.85
  }
}
```

### `POST /api/predict/batch`
Make batch predictions

### `GET /api/features`
Get feature information and valid values

## 🧪 Testing

### Test the API:
```bash
cd backend
python src/predict.py
```

### Test with Postman or curl:
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    ...
  }'
```

## 📦 Dependencies

### Backend
- Flask 3.0.0
- pandas 2.1.4
- scikit-learn 1.3.2
- xgboost 2.0.3
- joblib 1.3.2

### Frontend
- React 18.2.0
- Axios 1.6.2

## 🎯 Key Features of the Implementation

1. **Modular Architecture**: Separated concerns with clear file structure
2. **Preprocessing Pipeline**: Automated data cleaning and feature engineering
3. **Model Selection**: Automatic selection of best performing model
4. **REST API**: Clean API design with proper error handling
5. **Responsive UI**: Mobile-friendly React interface
6. **Real-time Predictions**: Fast inference with probability scores
7. **Actionable Insights**: Recommendations for high-risk customers

## 🔧 Troubleshooting

### Model not found error:
Run `python models/train_model.py` to train and save the model

### CORS errors:
Check that CORS_ORIGINS in config.py includes your frontend URL

### Port already in use:
Change the port in config.py or .env file

## 📈 Future Enhancements

- Add model explainability (SHAP values)
- Implement user authentication
- Add batch upload functionality
- Create admin dashboard for monitoring
- Deploy to cloud (AWS/GCP/Azure)
- Add A/B testing capabilities

## 📄 License

This project is open source and available for educational purposes.

## 👥 Contributing

Feel free to fork this project and submit pull requests for any improvements.

---

**Built with ❤️ using React, Flask, and scikit-learn**