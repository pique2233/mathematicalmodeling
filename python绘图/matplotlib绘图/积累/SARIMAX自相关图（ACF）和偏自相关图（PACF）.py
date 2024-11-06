import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# 生成一个示例时间序列数据
np.random.seed(42)
date_rng = pd.date_range(start='2020-01-01', end='2022-12-01', freq='M')
data = np.random.randn(len(date_rng)) + np.linspace(0, 10, len(date_rng))
ts_data = pd.Series(data, index=date_rng)

# 绘制自相关图 (ACF Plot)
plt.figure(figsize=(14, 7))
plot_acf(ts_data, lags=15, alpha=0.05)
plt.title("Autocorrelation Function (ACF)")
plt.show()

# 绘制偏自相关图 (PACF Plot)
plt.figure(figsize=(14, 7))
plot_pacf(ts_data, lags=15, alpha=0.05)
plt.title("Partial Autocorrelation Function (PACF)")
plt.show()