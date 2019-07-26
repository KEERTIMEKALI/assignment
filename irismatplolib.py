import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\HP\\Desktop\\iris.csv")

print(df.head(10))

df.describe()

plt.figure(figsize=(10, 7))
x = df["SepalLengthCm"]
plt.hist(x, bins=20, color="green")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count")

plt.figure(figsize=(10, 7))
x = df.SepalWidthCm
plt.hist(x, bins=20, color="green")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10, 7))
x = df.PetalWidthCm
plt.hist(x, bins=20, color="green")
plt.title("Petal Width in cm")
plt.xlabel("Petal_Width_cm")
plt.ylabel("Count")
plt.show()
