import matplotlib.pyplot as plt

# 示例数据
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 绘制折线图
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

categories = ['A', 'B', 'C', 'D']
values = [30, 50, 25, 40]

# 绘制条形图
plt.bar(categories, values, color='g')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

labels = ['Category A', 'Category B', 'Category C']
sizes = [40, 30, 20]

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.show()
