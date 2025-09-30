import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Data directories
DATA_DIR = BASE_DIR / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'

# Model directory
MODEL_DIR = BASE_DIR / 'models'

# File paths
RAW_DATA_PATH = RAW_DATA_DIR / 'churnRushi.csv'
PROCESSED_DATA_PATH = PROCESSED_DATA_DIR / 'processed_data.csv'
MODEL_PATH = MODEL_DIR / 'model.pkl'
SCALER_PATH = MODEL_DIR / 'scaler.pkl'

# Model parameters
TEST_SIZE = 0.2
RANDOM_STATE = 42

# API configuration
API_HOST = os.getenv('API_HOST', '0.0.0.0')
API_PORT = int(os.getenv('API_PORT', 5000))
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# CORS settings
CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:3000').split(',')

# Feature lists (most important features for prediction)
NUMERICAL_FEATURES = ['tenure', 'MonthlyCharges', 'TotalCharges']
CATEGORICAL_FEATURES = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents',
    'PhoneService', 'MultipleLines', 'InternetService',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies',
    'Contract', 'PaperlessBilling', 'PaymentMethod'
]