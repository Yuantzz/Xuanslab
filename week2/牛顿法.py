def square_root_2():
    # 初始猜测值
    guess = 1.0
    # 允许误差范围
    epsilon = 0.0001

    while abs(guess**2 - 2) > epsilon:
        # 使用牛顿迭代法更新猜测值
        guess = (guess + 2 / guess) / 2

    return guess

# 求解根号2并输出结果
result = square_root_2()
print(f"根号2 的近似值为: {result}")

