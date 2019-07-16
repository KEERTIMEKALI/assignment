import pandas as pd

df= pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data")
print(df)
print(df.head(2))
print(df.tail(2))
print(df.describe())
print(df.values)

print(df.axes)
print(df.groupby('1').groups)
