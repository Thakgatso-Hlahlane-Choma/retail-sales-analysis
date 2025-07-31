import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_sales_trend(df):
    """
    Plot total monthly sales trend over time.
    Expects a 'date' and 'total_amount' column.
    """
    df = df.copy()
    if 'date' not in df.columns or 'total_amount' not in df.columns:
        print(" Required columns 'date' and 'total_amount' not found.")
        return

    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    monthly_sales = df.groupby(df['date'].dt.to_period('M'))['total_amount'].sum().reset_index()
    monthly_sales['date'] = monthly_sales['date'].dt.to_timestamp()

    plt.figure(figsize=(10, 5))
    sns.lineplot(data=monthly_sales, x='date', y='total_amount', marker='o')
    plt.title(' Monthly Sales Trend')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_category_distribution(df):
    """
    Plot total sales per product category.
    Requires 'product_category' and 'total_amount' columns.
    """
    df = df.copy()
    if 'product_category' not in df.columns or 'total_amount' not in df.columns:
        print(" Required columns 'product_category' and 'total_amount' not found.")
        return

    category_sales = df.groupby('product_category')['total_amount'].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(y=category_sales.index, x=category_sales.values, palette='viridis')
    plt.title(' Total Sales by Product Category')
    plt.xlabel('Total Sales')
    plt.ylabel('Product Category')
    plt.tight_layout()
    plt.show()


def plot_gender_sales(df):
    """
    Plot total sales by gender.
    Requires 'gender' and 'total_amount' columns.
    """
    df = df.copy()
    if 'gender' not in df.columns or 'total_amount' not in df.columns:
        print(" Required columns 'gender' and 'total_amount' not found.")
        return

    gender_sales = df.groupby('gender')['total_amount'].sum().sort_values()

    plt.figure(figsize=(6, 4))
    sns.barplot(x=gender_sales.index, y=gender_sales.values, palette='Set2')
    plt.title(' Total Sales by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Total Sales')
    plt.tight_layout()
    plt.show()


def plot_age_distribution(df):
    """
    Plot age distribution of customers.
    Requires 'age' column.
    """
    df = df.copy()
    if 'age' not in df.columns:
        print(" 'age' column not found.")
        return

    plt.figure(figsize=(8, 4))
    sns.histplot(df['age'].dropna(), kde=True, bins=20, color='skyblue')
    plt.title(' Age Distribution of Customers')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
