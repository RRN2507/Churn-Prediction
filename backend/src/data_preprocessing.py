import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_data(filepath):
    """Load the dataset from CSV file."""
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    """Clean the dataset by handling missing values and data type issues."""
    df = df.copy()
    
    # Remove customerID as it's not useful for prediction
    if 'customerID' in df.columns:
        df = df.drop('customerID', axis=1)
    
    # Convert TotalCharges to numeric (some values might be spaces)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    
    # Fill missing TotalCharges with 0 (typically for new customers)
    df['TotalCharges'].fillna(0, inplace=True)
    
    # Convert SeniorCitizen to string for consistency
    df['SeniorCitizen'] = df['SeniorCitizen'].astype(str)
    
    return df

def encode_features(df, label_encoders=None, fit=True):
    """Encode categorical features using Label Encoding."""
    df = df.copy()
    
    # Separate target variable if present
    target = None
    if 'Churn' in df.columns:
        target = df['Churn'].copy()
        df = df.drop('Churn', axis=1)
    
    # Get categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    if fit:
        label_encoders = {}
        for col in categorical_cols:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le
    else:
        if label_encoders is None:
            raise ValueError("label_encoders must be provided when fit=False")
        for col in categorical_cols:
            if col in label_encoders:
                df[col] = label_encoders[col].transform(df[col].astype(str))
    
    # Encode target variable
    if target is not None:
        if fit:
            target_encoder = LabelEncoder()
            target_encoded = target_encoder.fit_transform(target)
            label_encoders['Churn'] = target_encoder
        else:
            target_encoded = label_encoders['Churn'].transform(target)
        
        df['Churn'] = target_encoded
    
    return df, label_encoders

def scale_features(df, scaler=None, fit=True, exclude_cols=None):
    """Scale numerical features using StandardScaler."""
    df = df.copy()
    
    if exclude_cols is None:
        exclude_cols = ['Churn'] if 'Churn' in df.columns else []
    
    # Get columns to scale
    cols_to_scale = [col for col in df.columns if col not in exclude_cols]
    
    if fit:
        scaler = StandardScaler()
        df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
    else:
        if scaler is None:
            raise ValueError("scaler must be provided when fit=False")
        df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    
    return df, scaler

def preprocess_data(filepath, label_encoders=None, scaler=None, fit=True):
    """Complete preprocessing pipeline."""
    # Load data
    df = load_data(filepath)
    
    # Clean data
    df = clean_data(df)
    
    # Encode features
    df, label_encoders = encode_features(df, label_encoders, fit)
    
    # Scale features
    df, scaler = scale_features(df, scaler, fit)
    
    return df, label_encoders, scaler

def prepare_input_data(input_dict, label_encoders, scaler):
    """Prepare single input for prediction."""
    # Create DataFrame from input
    df = pd.DataFrame([input_dict])
    
    # Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(0, inplace=True)
    
    # Convert SeniorCitizen to string
    df['SeniorCitizen'] = df['SeniorCitizen'].astype(str)
    
    # Encode features
    df, _ = encode_features(df, label_encoders, fit=False)
    
    # Scale features
    df, _ = scale_features(df, scaler, fit=False)
    
    return df