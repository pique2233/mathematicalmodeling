import pandas as pd
import numpy as np

# 加载Excel文件
file_path = '/mnt/data/1.22xlsx.xlsx'  # 替换为你的文件路径
data = pd.read_excel(file_path)

# 提取成分数据的列（排除非成分的列）
composition_columns = [
    '二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)', '氧化镁(MgO)',
    '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)', '氧化钡(BaO)',
    '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)'
]

# 提取成分数据
composition_data = data[composition_columns]

# 进行CLR变换
# 计算几何平均值
geo_mean = composition_data.apply(lambda x: np.exp(np.mean(np.log(x[x > 0]))), axis=1)

# CLR变换
clr_data = np.log(composition_data.div(geo_mean, axis=0))

# 将变换后的数据与原始数据合并
clr_data.columns = [f"CLR({col})" for col in clr_data.columns]
processed_data = pd.concat([data, clr_data], axis=1)

# 保存处理后的数据为新的Excel文件
output_path = '/mnt/data/CLR_processed_data.xlsx'  # 替换为你希望保存的文件路径
processed_data.to_excel(output_path, index=False)