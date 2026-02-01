from random import randint

import F1_20 as F

Rows: int = randint(1, 10)
Cols: int = randint(1, 10)
A = F.np.random.randint(1, 10, (Rows, Cols))
