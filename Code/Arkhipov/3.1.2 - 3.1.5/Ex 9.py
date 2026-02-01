from random import randint

import F1_20 as F

N = 10  # Col
M = 10  # Row
A = F.np.array([[randint(0, 10) for _ in range(N)] for _ in range(M)])
print(f"A({M}x{N} = \n{A}\n")
Value1 = 2
Value2 = 0
B = F.replace_except_value(A, Value1, Value2)
print(f"Value to preserve: {Value1}, Value to place: {Value2}\n{B})")
