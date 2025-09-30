import pandas as pd

def create_features(df):
    """Create additional features for better prediction."""
    df = df.copy()
    
    # Average charges per month
    df['AvgCharges'] = df['TotalCharges'] / (df['tenure'] + 1)  # +1 to avoid division by zero
    
    # Service count (number of additional services)
    service_cols = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
                    'TechSupport', 'StreamingTV', 'StreamingMovies']
    
    # Before encoding, count 'Yes' values
    if df[service_cols[0]].dtype == 'object':
        df['ServiceCount'] = df[service_cols].apply(lambda x: (x == 'Yes').sum(), axis=1)
    else:
        # After encoding, 'Yes' might be 1 or another value
        df['ServiceCount'] = df[service_cols].sum(axis=1)
    
    # Tenure groups
    if df['tenure'].dtype in ['int64', 'float64']:
        df['TenureGroup'] = pd.cut(df['tenure'], 
                                   bins=[-1, 12, 24, 48, 100],
                                   labels=[0, 1, 2, 3],
                                   include_lowest=True)
        df['TenureGroup'] = df['TenureGroup'].cat.codes
    
    # Monthly charges groups
    if df['MonthlyCharges'].dtype in ['int64', 'float64']:
        df['ChargeGroup'] = pd.cut(df['MonthlyCharges'],
                                   bins=[-1, 35, 70, 100, 200],
                                   labels=[0, 1, 2, 3],
                                   include_lowest=True)
        df['ChargeGroup'] = df['ChargeGroup'].cat.codes
    
    return df

def select_important_features(df, feature_importance=None, top_n=15):
    """Select most important features based on feature importance."""
    if feature_importance is not None and 'Churn' in df.columns:
        # Get top N features
        top_features = feature_importance.nlargest(top_n).index.tolist()
        top_features.append('Churn')  # Always include target
        df = df[top_features]
    
    return df