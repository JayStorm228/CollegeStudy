import F1_20 as F

Rows = 5
Cols = 5
A = F.np.random.randint(1, 10, (Rows, Cols))
Max: int = int(F.array_max(A))
CountMax: int = F.count_value_in_array(A, Max)

print(f"A({Rows}x{Cols}) = \n{A}\n{Max=}, Amount = {CountMax} ")
