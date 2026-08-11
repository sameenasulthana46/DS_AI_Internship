import numpy as np

A = np.array([[1, 2],
              [3, 4]])

result = np.linalg.det(A)

print("Determinant:")
print(result)