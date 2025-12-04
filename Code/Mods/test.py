<<<<<<< HEAD
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
=======
>>>>>>> 8118e5b3a7d2234fd7fa510cdec7f538f9fd1409
