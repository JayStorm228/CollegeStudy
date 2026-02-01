from random import randint

import F1_20 as F

N = 10
A: list[int] = [randint(0, 10) for w in range(N)]
MaxValue: int = F.get_list_max(A)
MaxCount: int = F.count_max_elements(A)
print(
    f"N = {N}, A = {A}\nMaximum value: {MaxValue}, amount of these values: {MaxCount}"
)
