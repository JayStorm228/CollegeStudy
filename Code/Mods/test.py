print(
    """
Эта программа вычисляет значение функции на промежутке
F = cos(1/x) + 2 tg(x)
промежуток: от 1 до 8 с шагом 0.5
"""
)
import math

start = 1
end = 6
step = 0.5

x = start
while x <= end:
    y = x - math.sin(x) + 3 * math.tan(x)
    print(f"x = {x:.1f}, y = {y:.4f}")
    x += step
