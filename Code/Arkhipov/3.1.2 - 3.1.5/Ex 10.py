from random import randint

import F1_20 as F

N = 10
A: list[int] = sorted([randint(0, 10) for w in range(N)])
print(f"N = {N}, A = {A}")
Value = 4
A = F.append_and_sort(A, Value)
print(f"Value to insert: {Value}\n{A}\n")
