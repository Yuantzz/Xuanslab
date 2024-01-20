import random
import math

def monte_carlo_integration(func, a, b, num_samples=1000000):
    integral_sum = 0

    for _ in range(num_samples):
        x = random.uniform(a, b)
        integral_sum += func(x)

    integral_approximation = (b - a) * (integral_sum / num_samples)
    return integral_approximation

def target_function(x):
    return x**2 + 4 * x * math.sin(x)

# 区间 [a, b]
a = 2
b = 3

result = monte_carlo_integration(target_function, a, b)
print(f"蒙特卡洛法估计的定积分值: {result}")
