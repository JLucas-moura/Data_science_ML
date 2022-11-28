# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 06:36:50 2022

@author: myjoa
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics


# Lendo os dados
xls = pd.ExcelFile('heart_disease.xlsx')
df = pd.read_excel(xls, 'data')

# modelos preditivos
# regressão, arvore de decisão, Randon Forest e Support Vector Machines

# creating dummies
data_model = pd.DataFrame({"HeartDisease": np.where(df["HeartDisease"] == "Yes", 1, 0),
                           "Smoking": np.where(df["Smoking"] == "Yes", 1, 0),
                           "AlcoholDrinking": np.where(df["AlcoholDrinking"] == "Yes", 1, 0),
                           "Stroke": np.where(df["Stroke"] == "Yes", 1, 0),
                           "DiffWalking": np.where(df["DiffWalking"] == "Yes", 1, 0),
                           "Sex": np.where(df["Sex"] == "Yes", 1, 0),
                           "PhysicalActivity": np.where(df["PhysicalActivity"] == "Yes", 1, 0),
                           "KidneyDisease": np.where(df["KidneyDisease"] == "Yes", 1, 0),
                           "SkinCancer": np.where(df["SkinCancer"] == "Yes", 1, 0),
                           "Asthma": np.where(df["Asthma"] == "Yes", 1, 0)})

data_model["BMI"] = df["PhysicalHealth"]
data_model["PhysicalHealth"] = df["PhysicalHealth"]
data_model["MentalHealth"] = df["MentalHealth"]
data_model["SleepTime"] = df["SleepTime"]

# last categorical
data_model["AgeCategory"] = df["AgeCategory"]
data_model["Race"] = df["Race"]
data_model["Diabetic"] = df["Diabetic"]
data_model["GenHealth"] = df["GenHealth"]

data_model = pd.get_dummies(data_model)
 
# Creating model
y = data_model.HeartDisease
X = data_model.drop("HeartDisease", axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))