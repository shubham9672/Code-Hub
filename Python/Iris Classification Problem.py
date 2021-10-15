"""THE FAMOUS IRIS CLASSIFICATION PROBLEM"""
""""by: Titan1911(Sahil Ahuja)"""
"""
This is simple ML model. It is based on the iris data set. The model predicts the type of the flower according to the data
provided. It has 3 flower types namely: setosa, versicolor and virginica. The data set is based on 4 features of a flower
namely: sepal length, sepal width, petal length and petal width. The model uses Linear Regression, provides with an
accuracy of 93 percent and is able to classify the type of flower.
"""

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()

features = iris.feature_names

X = iris.data
X.shape

y = iris.target
y.shape

i = 3  # the i factor is just for the visualization of the particular feature using the box plot. ranges from 0 to 3.
sns.boxplot(x=iris.target, y=iris.data[:, i])
title = "Class Variation With Respect to " + features[i]
plt.title(title)
plt.xlabel("Output Class")
plt.ylabel(features[i])
plt.show()

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

print(lin_model.coef_)
weights = lin_model.coef_
print("Most important feature is :", features[abs(weights).argmax()])
print("Least Imporant feature is:", features[abs(weights).argmin()])

print(lin_model.score(X_test, y_test))

prediction = lin_model.predict(X_test)
