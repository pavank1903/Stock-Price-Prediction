# -*- coding: utf-8 -*-
"""stock_prediction1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FgSAdKs2iXEBbYk4YISoaH2qsL_uVqHw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
from plotly.offline import plot
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
d=pd.read_csv('/content/stock1.csv')
print(d)

d.head(5)

d.info()

d.describe()

df = pd.DataFrame(d, columns=[ "Volume" , "Open"])
df.plot(x="Open", y=["Volume"], figsize=(35, 18))
plt.show()

df = pd.DataFrame(d, columns=["High", "Date"])
df.plot(x="Date", y=["High"], figsize=(9, 8))
plt.show()

df = pd.DataFrame(d, columns=["Volume", "Date"])
df.plot(x="Date", y=["Volume"], figsize=(10, 8))
plt.show()

d['Open'].plot(figsize=(16,6))



plt.figure(figsize=(20,12))
plt.subplot(2,1,1)
plt.title('stock price')
plt.plot(d.High,label='Close')
plt.legend()
plt.show()

d.to_csv("cleaned_data")

d.corr()

d.cov()

for column in d.columns:
  print(d[column].value_counts())
  print("*"*20)

d.describe()

d[['Open','High','Low','Close']].plot(kind='bar')

d['Volume'].value_counts()

d.shape

d

d.drop(columns=['Date'],inplace=True)

"""Cleaned data"""

d.head()

d.to_csv("Cleaned_data.csv")

x=d.drop(columns=['Volume'])
y=d['Volume']

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression, Lasso, Ridge 
from sklearn.preprocessing import OneHotEncoder, StandardScaler ,MinMaxScaler

from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline 
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error as mse,r2_score
import matplotlib.pyplot as plt
from sklearn import metrics

X=np.array(d.index).reshape(-1,1)
y=d['Close']

import pandas as pd
df = pd.read_csv('stock1.csv')

print(df.isnull().sum())

df = df.dropna()
print(df.isnull().sum())

"""Applying LinearRegression"""

X = d.drop('Volume', axis=1) 
y = d['Volume']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)


regressor = LinearRegression()


regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
y_pred

regressor.predict(X_test)

"""Decision Trees

"""

from sklearn.tree import DecisionTreeClassifier

from sklearn.tree import DecisionTreeRegressor

clf = DecisionTreeRegressor()


clf = clf.fit(X_train,y_train)


y_pred = clf.predict(X_test)
y_pred
from sklearn.metrics import mean_squared_error
print("Mean Squared Error:", metrics.mean_squared_error(y_test, y_pred))

from sklearn import tree
tree.plot_tree(clf,filled=True)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

"""KNN"""

from sklearn.neighbors import KNeighborsClassifier

X = d.drop('Volume', axis=1) 
y = d['Volume'] 


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)


k = 3
clf = KNeighborsClassifier(n_neighbors=k)

clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)
print("Mean Squared Error:", metrics.mean_squared_error(y_test, y_pred))
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

"""SVM"""

from sklearn.svm import SVC

X = d.drop('Volume', axis=1)
y = d['Volume'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

clf = SVC(kernel='linear')


clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)
print(y_pred)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))