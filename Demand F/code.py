import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX

from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv(r"C:\Demand F\train.csv")
df["Date"] = pd.to_datetime(df["Date"])
weekly = df.groupby("Date")["Weekly_Sales"].sum().reset_index()
weekly = weekly.sort_values("Date")
weekly.set_index("Date", inplace=True)
weekly.head()


plt.plot(weekly["Weekly_Sales"])
plt.title("Weekly Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()


decomp = seasonal_decompose(weekly["Weekly_Sales"], model="additive", period=52)
decomp.plot()
plt.show()

result = adfuller(weekly["Weekly_Sales"])
print(f"ADF Statistic: {result[0]}")
print(f"p-value: {result[1]}")

plot_acf(weekly["Weekly_Sales"])
plt.show()

plot_pacf(weekly["Weekly_Sales"])
plt.show()

model = SARIMAX(
    weekly['Weekly_Sales'],
    order=(1,0,1),
    seasonal_order=(1,0,1,52),
    enforce_stationarity=False,
    enforce_invertibility=False
)
fit = model.fit()
fit.summary()

forecast = fit.get_forecast(steps=52)
pred = forecast.predicted_mean
conf = forecast.conf_int()

plt.figure(figsize=(12,5))
plt.plot(weekly['Weekly_Sales'], label='Actual')
plt.plot(pred, label='Forecast', color='red')
plt.fill_between(conf.index, conf.iloc[:,0], conf.iloc[:,1], color='pink', alpha=0.3)
plt.legend()
plt.show()



import pandas as pd

# Combine predicted mean and confidence intervals
forecast_df = pd.DataFrame({
    'Date': pred.index,
    'Forecast': pred.values,
    'Lower_CI': conf.iloc[:,0].values,
    'Upper_CI': conf.iloc[:,1].values
})

# Optional: reset index
forecast_df.reset_index(drop=True, inplace=True)
forecast_df.head()

forecast_df.to_excel(r"C:\Demand F\Weekly_Sales_Forecast.xlsx", index=False)
print("Forecast saved to Excel successfully!")
