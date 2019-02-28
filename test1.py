import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('C:/Users/Hp-PC/Desktop/python/Telecom_customer_churn.csv')
X = df.iloc[:,55].values
n_Points = 900000.
dx = np.nanmax(X)/n_Points
y = []
string = ""
for i in range(0,len(X)):
	if(np.isnan(X[i])):
		y.append('null')
	if(~np.isnan(X[i])):
		string = "from %.2f to %.2f"%(int(X[i]/dx)*dx, int(X[i]/dx)*dx+dx)
		y.append(string)
		#print(X[i])
	
X1 = pd.DataFrame({"amount" : X, "range": y})
print(X1.groupby("range").count().sort_values(by = "amount", ascending = False))
X1.groupby('range').count().hist(bins = 100)
plt.show()

'''
y1 = np.zeros(shape = len(X))
y2 = []
j = 0
for i in range(0, len(X)):
	if(~np.isnan(X[i])):
		if(y2.count(int(X[i]/dx)) == 0):
			y1[j] += 1
			j += 1
			y2.append(int(X[i]/dx))
		else:
			y1[y2.index(int(X[i]/dx))] += 1

plt.scatter(X,y1)
plt.show()
'''