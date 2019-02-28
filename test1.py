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
