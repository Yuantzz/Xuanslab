def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# 获取用户输入
user_input = int(input("请输入一个正整数 n: "))

# 计算阶乘并输出结果
result = factorial(user_input)
print(f"{user_input} 的阶乘是: {result}")
