from random import randint

import F1_20 as F

N = 10  # Col
M = 10  # Row
A = F.np.array([[randint(0, 10) for _ in range(N)] for _ in range(M)])
Scale = 2
B = F.scale_array(A, Scale)
print(f"A({M}x{N}) = \n{A}\nScale = {Scale}: \n{B}\n ")
