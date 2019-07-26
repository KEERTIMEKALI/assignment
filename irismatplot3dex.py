import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("C:\\Users\\HP\\Desktop\\iris.csv")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = [data["PetalWidthCm"], data["PetalLengthCm"]]
n = 100
ax.scatter(data["PetalWidthCm"], data["PetalLengthCm"], data["SepalLengthCm"])
ax.set_xlabel('PetalWidthCm')
ax.set_ylabel('PetalLengthCm')
ax.set_zlabel('SepalLengthCm')

plt.tight_layout(pad=0.5)
plt.show()