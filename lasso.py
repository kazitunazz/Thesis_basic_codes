
# Importing required packages
import numpy as np
 
from sklearn.datasets import load_boston
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LassoCV
 
# Load the boston dataset.
boston = load_boston()
 
# Getting the meta-information
print(boston.DESCR)

# Printing the feature names 
print(boston.feature_names)


# Getting the data and target variable
X, y = boston['data'], boston['target']
 
# We use the base estimator LassoCV
clf = LassoCV(cv=3)
 
# Set a minimum threshold of 0.70
sfm = SelectFromModel(clf, threshold=0.70)
sfm.fit(X, y)
n_features = sfm.transform(X).shape[1]
 
# Extracting the index of important features
feature_idx = sfm.get_support()
 
# Using the index to print the names of the important variables
boston.feature_names[feature_idx]

print(boston.feature_names[feature_idx])
