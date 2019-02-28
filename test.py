import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from perceptron import Perceptron
import plot

df = pd.read_csv('C:/Users/Hp-PC/Desktop/Desktop/iris.csv')
y = df.iloc[1:101,4]
y = np.where(y == 'Setosa', -1, 1)

X = df.iloc[1:101, [0,2]]
X1 = np.array(X, dtype = np.float32)
ppn = Perceptron(eta = 0., n_iter = 10)
ppn.fit(X1, y)

plot.plot_decision_regions(X1, y, classifier = ppn)
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.legend(loc = 'upper left')
plt.show()
