import pandas as pd
x={"math":80,"Science":85,"English":80}
y=pd.Series(x)
print(y)
print(y[y>80]) #Selection
print(y.loc[["English"]])