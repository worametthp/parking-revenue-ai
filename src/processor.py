import pandas as pd

def prepare_features(df):
    df = df.copy()
    df['sales_date'] = pd.to_datetime(df['sales_date'])
    df['day_of_week'] = df['sales_date'].dt.dayofweek
    df['month'] = df['sales_date'].dt.month
    df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)
    
    return df