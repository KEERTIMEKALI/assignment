import pandas as pd

df=pd.read_csv("iris.data")
print(df)

d=df.describe()
print("Description \n",d)

print("data without index\n")
print(df.to_csv(sep='\t', index=False))

print("based on target -grouping")
print(df.groupby('Iris-setosa').groups)



print("First two colums\n",df.head(2))
print("Last two cloumns\n",df.tail(2))

print("Iris data axes",df.axes)


print("lungcancer data")
lf=pd.read_csv("lung-cancer.data")
print(lf)
l=lf.describe()
print("Description \n",l)

print("\n wine data")
wf=pd.read_csv("wine.data")
print(wf)
w=wf.describe()
print("Description \n",w)