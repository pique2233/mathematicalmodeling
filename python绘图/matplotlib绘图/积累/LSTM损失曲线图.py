import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# 生成示例数据
np.random.seed(42)
time_steps = np.linspace(0, 50, 500)
data = np.sin(time_steps) + np.random.normal(0, 0.1, len(time_steps))

# 数据预处理
scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data.reshape(-1, 1))

# 创建输入输出序列
X = []
y = []
seq_length = 10
for i in range(len(data_scaled) - seq_length):
    X.append(data_scaled[i:i+seq_length])
    y.append(data_scaled[i+seq_length])

X = np.array(X)
y = np.array(y)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 构建LSTM模型
model = Sequential()
model.add(LSTM(50, return_sequences=False, input_shape=(X_train.shape[1], 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# 训练模型
history = model.fit(X_train, y_train, epochs=20, batch_size=16, validation_data=(X_test, y_test), verbose=0)

# 预测
y_pred = model.predict(X_test)


color_palette = plt.get_cmap('tab10')

# 损失曲线图 (Loss Curve Plot)
plt.figure(figsize=(14, 7))
plt.plot(history.history['loss'], label='Train Loss', color=color_palette(0), linewidth=2)
plt.plot(history.history['val_loss'], label='Validation Loss', color=color_palette(1), linewidth=2)
plt.title('Loss Curve', fontsize=18, fontweight='bold')
plt.xlabel('Epochs', fontsize=14)
plt.ylabel('Loss', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()

# 预测 vs 真实值图 (Prediction vs Actual Plot)
plt.figure(figsize=(14, 7))
plt.plot(scaler.inverse_transform(y_test.reshape(-1, 1)), label='Actual', color=color_palette(2), linewidth=2)
plt.plot(scaler.inverse_transform(y_pred), label='Prediction', color=color_palette(3), linewidth=2, linestyle='--')
plt.title('Prediction vs Actual', fontsize=18, fontweight='bold')
plt.xlabel('Time Steps', fontsize=14)
plt.ylabel('Value', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()

# 时间步长注意力图 (Attention Weight Plot) -- 示例化，实际LSTM模型未实现注意力机制
attention_weights = np.random.rand(seq_length)  # 生成示例注意力权重
plt.figure(figsize=(14, 7))
bars = plt.bar(range(seq_length), attention_weights, color=color_palette(4))
plt.title('Attention Weights for Each Time Step', fontsize=18, fontweight='bold')
plt.xlabel('Time Steps', fontsize=14)
plt.ylabel('Attention Weight', fontsize=14)
plt.grid(True)
plt.show()
