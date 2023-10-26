def find_max_product(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    result = [[] for _ in range(n + 1)]
    result[1] = [1]

    for i in range(2, n + 1):
        for j in range(1, i):
            tmp = j * dp[i - j]
            if tmp > dp[i]:
                dp[i] = tmp
                result[i] = result[i - j] + [j]
        if not result[i]:
            result[i] = result[i - 1] + [1]

    return result[n]


n = 4
result = find_max_product(n)
print(result)

n = 5
result = find_max_product(n)
print(result)

# 代码的基础是建立在分解为质数2、3的乘积最后最大上的
