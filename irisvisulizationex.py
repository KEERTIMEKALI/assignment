# plotting the Iris dataset
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
# load the iris dataset
# print("Keys:", iris.keys())
# print keys of dataset

# shape of data and target
# print("Data shape", iris.data.shape) # (150, 4)
# print("Target shape", iris.target.shape) # (150,)

# print("data:", iris.data[:4]) # first 4 elements

# # unique targets
# print("Unique targets:", np.unique(iris.target)) # [0, 1, 2]
# # counts of each target
# print("Bin counts for targets:", np.bincount(iris.target))

# print("Feature names:", iris.feature_names)
# print("Target names:", iris.target_names)

colors = ['blue', 'red', 'green']
# # plot histogram
# for feature in range(iris.data.shape[1]): # (shape = 150, 4)
    # plt.subplot(2, 2, feature+1) # subplot starts from 1 (not 0)
    # for label, color in zip(range(len(iris.target_names)), colors):
        # # find the label and plot the corresponding data
        # plt.hist(iris.data[iris.target==label, feature],
                 # label=iris.target_names[label],
                 # color=color)
    # plt.xlabel(iris.feature_names[feature])
    # plt.legend()

# plot scatter plot : petal-width vs all features
feature_x= 0 # petal width
for feature_y in range(iris.data.shape[1]):
    plt.subplot(2, 2, feature_y+1) # subplot starts from 1 (not 0)
    for label, color in zip(range(len(iris.target_names)), colors):
        # find the label and plot the corresponding data
        plt.scatter(iris.data[iris.target==label, feature_x],
                    iris.data[iris.target==label, feature_y],
                    label=iris.target_names[label],
                    alpha = 0.45, # transparency
                    color=color)
    plt.xlabel(iris.feature_names[feature_x])
    plt.ylabel(iris.feature_names[feature_y])
    plt.legend()
plt.show()

feature_x= 1 # petal width
for feature_y in range(iris.data.shape[1]):
    plt.subplot(2, 2, feature_y+1) # subplot starts from 1 (not 0)
    for label, color in zip(range(len(iris.target_names)), colors):
        # find the label and plot the corresponding data
        plt.scatter(iris.data[iris.target==label, feature_x],
                    iris.data[iris.target==label, feature_y],
                    label=iris.target_names[label],
                    alpha = 0.45, # transparency
                    color=color)
    plt.xlabel(iris.feature_names[feature_x])
    plt.ylabel(iris.feature_names[feature_y])
    plt.legend()
plt.show()

feature_x= 2 # petal width
for feature_y in range(iris.data.shape[1]):
    plt.subplot(2, 2, feature_y+1) # subplot starts from 1 (not 0)
    for label, color in zip(range(len(iris.target_names)), colors):
        # find the label and plot the corresponding data
        plt.scatter(iris.data[iris.target==label, feature_x],
                    iris.data[iris.target==label, feature_y],
                    label=iris.target_names[label],
                    alpha = 0.45, # transparency
                    color=color)
    plt.xlabel(iris.feature_names[feature_x])
    plt.ylabel(iris.feature_names[feature_y])
    plt.legend()
plt.show()

feature_x= 3 # petal width
for feature_y in range(iris.data.shape[1]):
    plt.subplot(2, 2, feature_y+1) # subplot starts from 1 (not 0)
    for label, color in zip(range(len(iris.target_names)), colors):
        # find the label and plot the corresponding data
        plt.scatter(iris.data[iris.target==label, feature_x],
                    iris.data[iris.target==label, feature_y],
                    label=iris.target_names[label],
                    alpha = 0.45, # transparency
                    color=color)
    plt.xlabel(iris.feature_names[feature_x])
    plt.ylabel(iris.feature_names[feature_y])
    plt.legend()
plt.show()
