import numpy as np
import pandas as pd
from sklearn import tree
import pydot
from IPython.display import Image
from six import StringIO

input_file = "https://raw.githubusercontent.com/K-G-PRAJWAL/Machine-Learning-Projects/master/Hiring%20Prediction/PastHires.csv"
df = pd.read_csv(input_file, header=0)
print(df.head())

d = {"Y": 1, "N": 0}
df["Hired"] = df["Hired"].map(d)
df["Employed?"] = df["Employed?"].map(d)
df["Top-tier school"] = df["Top-tier school"].map(d)
df["Interned"] = df["Interned"].map(d)
d = {"BS": 0, "MS": 1, "PhD": 2}
df["Level of Education"] = df["Level of Education"].map(d)
print(df.head())


feature = list(df.columns[:6])
print(feature)

y = df["Hired"]
X = df[feature]

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(X, y)

dot_data = StringIO()
tree.export_graphviz(classifier, out_file=dot_data, feature_names=feature)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())


from sklearn.ensemble import RandomForestClassfier

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X, y)
# predicting  employed 10 year veteran
print(clf.predict([[10, 1, 4, 0, 0, 0]]))
# predicting an unemployed 10 year veteran
print(clf.predict([[10, 0, 4, 0, 0, 0]]))
