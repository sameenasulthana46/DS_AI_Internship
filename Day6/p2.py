import pandas as pd
import numpy as np
x=np.array([1,3,4,5])
y=pd.Series(x)
print(y.to_string())