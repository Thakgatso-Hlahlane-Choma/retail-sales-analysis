import pandas as pd
import os

def load_data(path):
    """Load dataset from a CSV file."""
    return pd.read_csv(path)

def clean_column_names(df):
    """Standardize column names."""
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(' ', '_')
                  .str.replace(r'[^\w\s]', '', regex=True)
    )
    return df

def basic_cleaning(df):
    """Apply essential data cleaning."""
    # Drop nulls in key columns
    essential_cols = ['transaction_id', 'date', 'product_category', 'quantity', 'total_amount']
    df = df.dropna(subset=[col for col in essential_cols if col in df.columns])

    # Fill missing values
    if 'product_category' in df.columns:
        df['product_category'] = df['product_category'].fillna('Unknown')

    # Convert dates
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Convert numerics
    for col in ['quantity', 'price_per_unit', 'total_amount']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df

def save_clean_data(df, path):
    """Save cleaned dataset to CSV."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
