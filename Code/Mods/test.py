print(
    f"""

"""
)
import math

a = float(input("a = "))
x = float(input("x = "))
if x < 1:
    print(a * math.log(x) + x ** (1 / 3))
elif 1 < x < 10:
    print(2 * a * math.cos(x) + 3 * x**2)
elif x > 10:
    print(5e-7 + math.tan(x))
