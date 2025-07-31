import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet


def prepare_time_series(df):
    """
    Prepares a DataFrame for time series forecasting with Prophet.

    Parameters:
    - df: DataFrame containing 'date' and 'total_amount'

    Returns:
    - DataFrame with 'ds' and 'y' columns for Prophet
    """
    df = df.copy()

    if 'date' not in df.columns or 'total_amount' not in df.columns:
        raise ValueError(" 'date' and 'total_amount' columns must be present in the DataFrame.")

    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    ts = df.groupby(df['date'].dt.to_period('M'))['total_amount'].sum().reset_index()
    ts['date'] = ts['date'].dt.to_timestamp()
    ts.columns = ['ds', 'y']
    return ts


def forecast_sales(ts_df, periods=6, plot=True):
    """
    Fits a Prophet model to the time series and forecasts future sales.

    Parameters:
    - ts_df: DataFrame with 'ds' and 'y' columns
    - periods: Number of months to forecast
    - plot: Whether to display forecast plots

    Returns:
    - Prophet forecast DataFrame
    """
    model = Prophet()
    model.fit(ts_df)

    future = model.make_future_dataframe(periods=periods, freq='M')
    forecast = model.predict(future)

    if plot:
        _plot_forecast(model, forecast)
        _plot_components(model, forecast)

    return forecast


def _plot_forecast(model, forecast):
    """Internal helper to plot the forecast."""
    fig = model.plot(forecast)
    plt.title(" Forecasted Sales")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()


def _plot_components(model, forecast):
    """Internal helper to plot forecast components (trend, seasonality)."""
    fig = model.plot_components(forecast)
    plt.tight_layout()
    plt.show()
