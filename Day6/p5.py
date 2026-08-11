import pandas as pd
scores = pd.Series([45,67,95,98,85])
passed = scores[scores > 60]
print(passed)