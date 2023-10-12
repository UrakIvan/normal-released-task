import math

V = float(input("Введіть початкову швидкість (V): "))
T = float(input("Введіть час польоту (T): "))

g = 9.81

alpha = math.asin((g * T) / (2 * V))

alpha_degrees = math.degrees(alpha)
print(f"Кут альфа під яким тіло було кинуто стосовно горизонту: {alpha_degrees} градусів")