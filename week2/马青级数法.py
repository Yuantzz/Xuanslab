def machin_series_pi():
    x = 1.0
    pi_approximation = 0.0
    epsilon = 1e-10
    sign = 1

    while abs(x) > epsilon:
        pi_approximation += sign * x
        x = x / 3
        sign = -sign

    return round(pi_approximation * math.sqrt(12), 10)

result_machin_series = machin_series_pi()
print(f"马青级数：{result_machin_series}")
