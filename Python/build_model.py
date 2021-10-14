#load in packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import time
import math

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

#Models
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestRegressor
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor


#use sklearn.metrics.mean_squared_error() AND math.sqrt() to get RMSE
from sklearn.metrics import mean_squared_error

#set a random_state to be used in the notebook
random_state = 7

#Example of RMSE
example_y_actual    = [10,20,30,40,50,60,70,80,90,100]
example_y_predicted = [12,20,35,45,50,30,50,80,92,95]
example_MSE = mean_squared_error(example_y_actual, example_y_predicted)
example_RMSE = math.sqrt(example_MSE)
print("Example Mean Squared Error:", round(example_MSE,1))
print("Example Root Mean Square Error:", round(example_RMSE,1))

#load in the data:
#source path 
path = '../input/'

#Get the metadata (the .csv data) and put it into DataFrames
train_df = pd.read_csv(path + 'train.csv')

#show the dimensions of the train metadata.
print('train_df dimensions: ', train_df.shape)
train_df.head(3)

y = train_df['label']
X = train_df['Feature']

#now make the train-test splits
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=random_state)
print('Dimensions: \n x_train:{} \n x_test{} \n y_train{} \n y_test{}'.format(x_train.shape, x_test.shape, y_train.shape, y_test.shape))

#create the Classifier
tree_clf = DecisionTreeClassifier(max_depth = 3, min_samples_split = 10)

#train the model
start = time.time()
tree_clf.fit(x_train, y_train)
stop = time.time()

#predict the response for the test data
tree_clf_pred = tree_clf.predict(x_test)

#print the RMSE
print(f'Training time: {round((stop - start),3)} seconds')
tree_clf_RMSE = math.sqrt(mean_squared_error(y_test, tree_clf_pred))
print(f'tree_clf_RMSE: {round(tree_clf_RMSE,3)}')
