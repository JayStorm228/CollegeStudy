from random import randint

import F1_20 as F

N = 10  # Col
M = 10  # Row
A = F.np.array([[randint(0, 10) for _ in range(N)] for _ in range(M)])
Critical = 4
CountCritical = F.count_greater_elements(A, Critical)
print(f"A({M}x{N}):\n{A}\nCritical Value = {Critical}, found: {CountCritical}")
