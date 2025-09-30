import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                            f1_score, roc_auc_score, confusion_matrix, 
                            classification_report)
from xgboost import XGBClassifier
import warnings
warnings.filterwarnings('ignore')

from src.data_preprocessing import preprocess_data
from src.feature_engineering import create_features
import config

def train_and_evaluate_models(X_train, X_test, y_train, y_test):
    """Train multiple models and return the best one."""
    
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=config.RANDOM_STATE),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=config.RANDOM_STATE),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=config.RANDOM_STATE),
        'XGBoost': XGBClassifier(n_estimators=100, random_state=config.RANDOM_STATE, eval_metric='logloss')
    }
    
    results = {}
    
    print("Training and evaluating models...\n")
    print("-" * 80)
    
    for name, model in models.items():
        print(f"\nTraining {name}...")
        
        # Train model
        model.fit(X_train, y_train)
        
        # Predictions
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        # Metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        
        results[name] = {
            'model': model,
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'roc_auc': roc_auc
        }
        
        print(f"Accuracy: {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1 Score: {f1:.4f}")
        print(f"ROC AUC: {roc_auc:.4f}")
    
    print("\n" + "-" * 80)
    
    # Find best model based on F1 score
    best_model_name = max(results, key=lambda x: results[x]['f1'])
    best_model = results[best_model_name]['model']
    
    print(f"\nBest Model: {best_model_name}")
    print(f"F1 Score: {results[best_model_name]['f1']:.4f}")
    
    return best_model, results

def main():
    """Main training pipeline."""
    
    print("Starting model training pipeline...\n")
    
    # Create directories if they don't exist
    config.MODEL_DIR.mkdir(parents=True, exist_ok=True)
    config.PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load and preprocess data
    print("Loading and preprocessing data...")
    df, label_encoders, scaler = preprocess_data(config.RAW_DATA_PATH, fit=True)
    
    # Create additional features
    print("Creating features...")
    df = create_features(df)
    
    # Save processed data
    df.to_csv(config.PROCESSED_DATA_PATH, index=False)
    print(f"Processed data saved to {config.PROCESSED_DATA_PATH}")
    
    # Split features and target
    X = df.drop('Churn', axis=1)
    y = df['Churn']
    
    print(f"\nDataset shape: {X.shape}")
    print(f"Churn distribution:\n{y.value_counts()}")
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config.TEST_SIZE, random_state=config.RANDOM_STATE, stratify=y
    )
    
    print(f"\nTrain set size: {X_train.shape}")
    print(f"Test set size: {X_test.shape}")
    
    # Train and evaluate models
    best_model, results = train_and_evaluate_models(X_train, X_test, y_train, y_test)
    
    # Final evaluation on best model
    print("\n" + "=" * 80)
    print("FINAL MODEL EVALUATION")
    print("=" * 80)
    
    y_pred = best_model.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['No Churn', 'Churn']))
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Save model and preprocessing objects
    print(f"\nSaving model to {config.MODEL_PATH}")
    joblib.dump(best_model, config.MODEL_PATH)
    
    print(f"Saving scaler to {config.SCALER_PATH}")
    joblib.dump(scaler, config.SCALER_PATH)
    
    # Save label encoders
    encoders_path = config.MODEL_DIR / 'label_encoders.pkl'
    print(f"Saving label encoders to {encoders_path}")
    joblib.dump(label_encoders, encoders_path)
    
    print("\n✅ Training completed successfully!")
    print(f"Model accuracy: {accuracy_score(y_test, y_pred):.4f}")
    
    return best_model, scaler, label_encoders

if __name__ == "__main__":
    main()