import numpy as np

A = np.array([[1, 2],
              [3, 4]])

result = np.linalg.inv(A)

print("Inverse:")
print(result)