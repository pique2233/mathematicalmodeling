import matplotlib.pyplot as plt
import seaborn as sns

# 散点图与回归拟合线 - 乙醇转化率
plt.figure(figsize=(10, 6))
sns.scatterplot(x='温度', y='乙醇转化率(%)', data=data1_cleaned, label='Actual')
sns.lineplot(x='温度', y='预测乙醇转化率', data=data1_cleaned, label='Predicted', color='red')
plt.title('Temperature vs Ethanol Conversion Rate')
plt.xlabel('Temperature (°C)')
plt.ylabel('Ethanol Conversion Rate (%)')
plt.legend()
plt.show()

# 散点图与回归拟合线 - C4烯烃选择性
plt.figure(figsize=(10, 6))
sns.scatterplot(x='温度', y='C4烯烃选择性(%)', data=data1_cleaned, label='Actual')
sns.lineplot(x='温度', y='预测C4烯烃选择性', data=data1_cleaned, label='Predicted', color='red')
plt.title('Temperature vs C4 Olefin Selectivity')
plt.xlabel('Temperature (°C)')
plt.ylabel('C4 Olefin Selectivity (%)')
plt.legend()
plt.show()