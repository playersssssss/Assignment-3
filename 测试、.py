import pandas as pd
import matplotlib.pyplot as plt

# 创建示例数据
data = {
    'Year': [2010, 2011, 2012, 2013, 2014],
    'Category A': [100, 120, 140, 160, 180],
    'Category B': [80, 100, 120, 140, 160],
    'Category C': [60, 80, 100, 120, 140]
}

df = pd.DataFrame(data)

# 设置年份列作为索引
df.set_index('Year', inplace=True)

# 绘制面积图
df.plot(kind='area', stacked=False, figsize=(10, 6))

# 添加标题和标签
plt.title('Sales Trends by Category (2010-2014)')
plt.xlabel('Year')
plt.ylabel('Sales')

# 显示图表
plt.show()



