# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 19:55:54 2019

@author: Admin
"""

# Support Vector Machine (SVM)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.io as sio

# Importing the dataset
#dataset = pd.read_csv('Social_Network_Ads.csv')
#X = dataset.iloc[:, [2, 3]].values
#y = dataset.iloc[:, 4].values
hyper_dict  = sio.loadmat('W:\ISRO\Isro\Indian_pines_corrected.mat')
hyper_data = hyper_dict['indian_pines_corrected']
hyper_truth = sio.loadmat('W:/ISRO/Isro/Indian_pines_gt.mat')
gt = hyper_truth['indian_pines_gt']

roi = gt >0
X =  hyper_data[gt > 0 ]
y = gt[roi]
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.7, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

from sklearn.metrics import classification_report

cr = classification_report(y_test,y_pred)
 from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

