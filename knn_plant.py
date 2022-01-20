'''
Tried using k nearest neighbor to determine what counted as a "high", "medium", or "low" reflective object. Such as concrete, wood, and fabric, respectivley. 
Did not go well...
'''


import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
from polynomial_reg import x5, y5, new_wallx5, new_wally5

n_neighbors = 3

# import some data to play with
iris = datasets.load_iris()

all_walls_x = new_wallx5
all_walls_y = new_wally5
all_wood_x = x5
all_wood_y = y5
all_x = all_walls_x + all_wood_x
all_y = all_walls_y + all_wood_y
result = [1] * len(all_walls_x) + [0] * len(all_wood_x)

lst = []
for i in range(len(all_x)):
    lst.append([all_x[i], all_y[i], result[i]])
random.shuffle(lst)

x_value = []
results = []
for j in range(len(lst)):
    x_value.append([lst[j][0], lst[j][1]])
    results.append(lst[j][2])

iris = {'data': np.array(x_value), 'target': np.array(results)}
print(iris)

X = iris['data'][:, :2]  # we only take the first two features. We could
                      # avoid this ugly slicing by using a two-dim dataset
y = iris['target']
h = .02  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))
    plt.xlim(left = 100, right = 300)
    plt.ylim(top = 2, bottom = 0)

plt.show()
