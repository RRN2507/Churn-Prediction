import joblib
import pandas as pd
import numpy as np
from pathlib import Path
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_preprocessing import prepare_input_data
from src.feature_engineering import create_features
import config

class ChurnPredictor:
    """Class to handle churn prediction."""
    
    def __init__(self):
        """Initialize the predictor by loading model and preprocessing objects."""
        self.model = None
        self.scaler = None
        self.label_encoders = None
        self.load_artifacts()
    
    def load_artifacts(self):
        """Load trained model and preprocessing objects."""
        try:
            self.model = joblib.load(config.MODEL_PATH)
            self.scaler = joblib.load(config.SCALER_PATH)
            encoders_path = config.MODEL_DIR / 'label_encoders.pkl'
            self.label_encoders = joblib.load(encoders_path)
            print("✅ Model and preprocessing objects loaded successfully")
        except FileNotFoundError as e:
            print(f"❌ Error loading artifacts: {e}")
            print("Please train the model first by running: python models/train_model.py")
            raise
    
    def predict(self, input_data):
        """
        Make prediction for a single input.
        
        Args:
            input_data (dict): Dictionary containing feature values
            
        Returns:
            dict: Prediction result with churn label and probability
        """
        # Prepare input
        df = prepare_input_data(input_data, self.label_encoders, self.scaler)
        
        # Create additional features
        df = create_features(df)
        
        # Make prediction
        prediction = self.model.predict(df)[0]
        probability = self.model.predict_proba(df)[0]
        
        # Decode prediction
        churn_label = self.label_encoders['Churn'].inverse_transform([prediction])[0]
        
        result = {
            'churn': churn_label,
            'churn_probability': float(probability[1]),
            'no_churn_probability': float(probability[0]),
            'confidence': float(max(probability))
        }
        
        return result
    
    def predict_batch(self, input_list):
        """
        Make predictions for multiple inputs.
        
        Args:
            input_list (list): List of dictionaries containing feature values
            
        Returns:
            list: List of prediction results
        """
        results = []
        for input_data in input_list:
            result = self.predict(input_data)
            results.append(result)
        return results

def test_predictor():
    """Test the predictor with sample data."""
    predictor = ChurnPredictor()
    
    # Sample input
    sample_input = {
        'gender': 'Male',
        'SeniorCitizen': 0,
        'Partner': 'Yes',
        'Dependents': 'No',
        'tenure': 12,
        'PhoneService': 'Yes',
        'MultipleLines': 'No',
        'InternetService': 'Fiber optic',
        'OnlineSecurity': 'No',
        'OnlineBackup': 'No',
        'DeviceProtection': 'No',
        'TechSupport': 'No',
        'StreamingTV': 'Yes',
        'StreamingMovies': 'Yes',
        'Contract': 'Month-to-month',
        'PaperlessBilling': 'Yes',
        'PaymentMethod': 'Electronic check',
        'MonthlyCharges': 85.0,
        'TotalCharges': 1020.0
    }
    
    print("\nTesting predictor with sample data:")
    print("-" * 50)
    print(f"Input: {sample_input}")
    
    result = predictor.predict(sample_input)
    
    print("\nPrediction Result:")
    print("-" * 50)
    print(f"Churn: {result['churn']}")
    print(f"Churn Probability: {result['churn_probability']:.2%}")
    print(f"No Churn Probability: {result['no_churn_probability']:.2%}")
    print(f"Confidence: {result['confidence']:.2%}")

if __name__ == "__main__":
    test_predictor()