def cube_root(num, epsilon=0.0001):
    guess = num / 2.0  # 初始猜测可以选择 num 的一半
    while abs(guess**3 - num) > epsilon:
        guess = guess - (guess**3 - num) / (3 * guess**2)
    return guess

# 获取用户输入
user_input = float(input("请输入一个数字: "))

# 求立方根并输出结果
result = cube_root(user_input)
print(f"{user_input} 的立方根是: {result}")
