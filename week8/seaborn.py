import seaborn as sns
import matplotlib.pyplot as plt

# 示例数据
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 使用 Seaborn 绘制折线图
sns.relplot(x=x, y=y)
plt.title('Line Chart (Seaborn)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

categories = ['A', 'B', 'C', 'D']
values = [30, 50, 25, 40]

# 使用 Seaborn 绘制条形图
sns.barplot(x=categories, y=values)
plt.title('Bar Chart (Seaborn)')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

n = [1, 2, 3, 4, 5]
m = [10, 20, 15, 25, 30]

# 使用 Seaborn 绘制散点图
sns.scatterplot(n=n, m=m)
plt.title('Scatter Plot (Seaborn)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
