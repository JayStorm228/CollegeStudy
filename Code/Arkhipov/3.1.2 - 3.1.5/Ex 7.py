from random import randint

import F1_20 as F

N = 10
A: list[int] = [randint(0, 10) for w in range(N)]
Position = 3
print(f"N = {N}, A = {A}, Position = {Position}")
F.remove_by_position(A, Position)
print(f"Modified A = {A}")
