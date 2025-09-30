from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback
import sys
import os

# Add the backend directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.predict import ChurnPredictor
import config

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": config.CORS_ORIGINS}})

# Initialize predictor
try:
    predictor = ChurnPredictor()
    print("✅ Churn Predictor initialized successfully")
except Exception as e:
    print(f"❌ Error initializing predictor: {e}")
    predictor = None

@app.route('/')
def home():
    """Home endpoint."""
    return jsonify({
        'message': 'Customer Churn Prediction API',
        'status': 'running',
        'version': '1.0.0'
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'model_loaded': predictor is not None
    })

@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Prediction endpoint.
    Expects JSON with customer features.
    """
    if predictor is None:
        return jsonify({
            'error': 'Model not loaded. Please train the model first.'
        }), 500
    
    try:
        # Get input data
        data = request.get_json()
        
        if not data:
            return jsonify({
                'error': 'No input data provided'
            }), 400
        
        # Validate required fields
        required_fields = [
            'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
            'PhoneService', 'MultipleLines', 'InternetService',
            'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
            'TechSupport', 'StreamingTV', 'StreamingMovies',
            'Contract', 'PaperlessBilling', 'PaymentMethod',
            'MonthlyCharges', 'TotalCharges'
        ]
        
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                'error': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400
        
        # Make prediction
        result = predictor.predict(data)
        
        # Return result
        return jsonify({
            'success': True,
            'prediction': result
        })
    
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            'error': f'Prediction failed: {str(e)}'
        }), 500

@app.route('/api/predict/batch', methods=['POST'])
def predict_batch():
    """
    Batch prediction endpoint.
    Expects JSON with list of customer features.
    """
    if predictor is None:
        return jsonify({
            'error': 'Model not loaded. Please train the model first.'
        }), 500
    
    try:
        # Get input data
        data = request.get_json()
        
        if not data or 'customers' not in data:
            return jsonify({
                'error': 'No input data provided. Expected {"customers": [...]}'
            }), 400
        
        customers = data['customers']
        
        if not isinstance(customers, list):
            return jsonify({
                'error': 'customers must be a list'
            }), 400
        
        # Make predictions
        results = predictor.predict_batch(customers)
        
        # Return results
        return jsonify({
            'success': True,
            'predictions': results,
            'count': len(results)
        })
    
    except Exception as e:
        print(f"Error during batch prediction: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            'error': f'Batch prediction failed: {str(e)}'
        }), 500

@app.route('/api/features', methods=['GET'])
def get_features():
    """Get information about required features."""
    feature_info = {
        'categorical_features': {
            'gender': ['Male', 'Female'],
            'SeniorCitizen': ['0', '1'],
            'Partner': ['Yes', 'No'],
            'Dependents': ['Yes', 'No'],
            'PhoneService': ['Yes', 'No'],
            'MultipleLines': ['Yes', 'No', 'No phone service'],
            'InternetService': ['DSL', 'Fiber optic', 'No'],
            'OnlineSecurity': ['Yes', 'No', 'No internet service'],
            'OnlineBackup': ['Yes', 'No', 'No internet service'],
            'DeviceProtection': ['Yes', 'No', 'No internet service'],
            'TechSupport': ['Yes', 'No', 'No internet service'],
            'StreamingTV': ['Yes', 'No', 'No internet service'],
            'StreamingMovies': ['Yes', 'No', 'No internet service'],
            'Contract': ['Month-to-month', 'One year', 'Two year'],
            'PaperlessBilling': ['Yes', 'No'],
            'PaymentMethod': ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']
        },
        'numerical_features': {
            'tenure': {'min': 0, 'max': 72, 'description': 'Months with company'},
            'MonthlyCharges': {'min': 0, 'max': 200, 'description': 'Monthly charges in dollars'},
            'TotalCharges': {'min': 0, 'max': 10000, 'description': 'Total charges in dollars'}
        }
    }
    
    return jsonify(feature_info)

if __name__ == '__main__':
    app.run(host=config.API_HOST, port=config.API_PORT, debug=config.DEBUG)