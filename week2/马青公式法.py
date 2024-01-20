import math

def machin_formula_pi():
    pi_approximation = 4 * (4 * math.atan(1/5) - math.atan(1/239))
    return round(pi_approximation, 10)

result_machin_formula = machin_formula_pi()
print(f"马青公式：{result_machin_formula}")
