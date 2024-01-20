import random

def monte_carlo_pi(num_samples=1000000):
    inside_circle = 0

    for _ in range(num_samples):
        x, y = random.random(), random.random()
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1

    pi_approximation = (inside_circle / num_samples) * 4
    return round(pi_approximation, 10)

result_monte_carlo = monte_carlo_pi()
print(f"蒙特卡洛方法：{result_monte_carlo}")
