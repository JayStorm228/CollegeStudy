import numpy as np

Matrix = Matrix = np.random.randint(1, 41, (5, 5))
Output = np.zeros((Matrix.shape[0], Matrix.shape[1]))
Size = Matrix.shape[0]
for w in range(Size):
    diag_elements = Matrix.diagonal(offset=w)
    indices = np.arange(len(diag_elements))
    Output[indices, indices + w] = diag_elements
print(Output)
