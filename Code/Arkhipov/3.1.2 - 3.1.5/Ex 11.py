from random import randint

import F1_20 as F

N = 10
A: list[int] = [randint(0, 10) for w in range(N)]
M = 10
B: list[int] = [randint(0, 10) for w in range(M)]
result: str = F.compare_products(A, B)
print(f"N = {N}, A = {A}\nM = {M}, B = {B}\n{result}")
