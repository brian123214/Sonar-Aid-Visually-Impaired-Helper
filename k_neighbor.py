import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from polynomial_reg import new_wallx3, new_wally3, new_wallx4, new_wally4, new_x, new_y, new_x2, new_y2
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets




n_neighbors = 15
all_walls_x = new_wallx3 + new_wallx4
all_walls_y = new_wally3 + new_wally4
all_wood_x = new_x + new_x2
all_wood_y = new_y + new_y2
all_x = all_walls_x + all_wood_x
all_y = all_walls_y + all_wood_y
result = [1] * len(all_walls_x) + [0] * len(all_wood_x)
data = {
    'x': all_x, 
    'y': all_y,
    'result': result
}
final_data = pd.DataFrame(data)
final_data =  final_data.sample(frac=1)
# print(final_data.head())
# inputs = 

print(len(all_x))

# inputs_train, inputs_test, result_train, result_test = train_test_split(inputs, result, random_state = 0)

# knn = KNeighborsClassifier(n_neighbors = 5)
# knn.fit(inputs_train,result_train)
# score = knn.score(inputs_test,result_test)
# print(score)


