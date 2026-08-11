import numpy as np

marks = np.array([[30, 60, 40],
                  [20, 60, 40],
                  [70, 80, 90]])

print("Marks:")
print(marks)

print("Mean:", np.mean(marks, axis=1))
print("Median:", np.median(marks, axis=1))
print("Standard Deviation:", np.std(marks))
print("Variance:", np.var(marks))
print("Shape:", marks.shape)

result = np.mean(marks, axis=1)
print("Mean Result:", result)
print("Result Shape:", result.shape)