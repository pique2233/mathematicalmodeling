import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
#观测数据、预测值和置信区间
# 生成样本时间序列数据
np.random.seed(0)
dates = pd.date_range(start='2020-01-01', periods=100, freq='M')
data = np.random.randn(100).cumsum() + 50

# 转换为DataFrame
df = pd.DataFrame(data, index=dates, columns=['Value'])

# 拟合SARIMAX模型
model = sm.tsa.SARIMAX(df['Value'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
results = model.fit()

# 预测
forecast = results.get_forecast(steps=12)
forecast_index = pd.date_range(start=df.index[-1], periods=12, freq='M')
forecast_values = forecast.predicted_mean.values
conf_int_values = forecast.conf_int().values

# 绘制原始数据和预测数据
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Value'], label='Observed', color='blue')
plt.plot(forecast_index, forecast_values, label='Forecast', color='red', linestyle='--')
plt.fill_between(forecast_index,
                 conf_int_values[:, 0],
                 conf_int_values[:, 1],
                 color='pink', alpha=0.3, label='Confidence Interval')
plt.title('SARIMAX Time Series Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
