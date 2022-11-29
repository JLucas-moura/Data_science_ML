import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
# from sklearn.metrics import confusion_matrix
from sklearn.linear_model import SGDClassifier
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import cross_val_predict
import matplotlib.pyplot as plt

data = pd.read_excel("heart_disease.xlsx", sheet_name="data")
print(data.columns)

# creating dummies
data_model = pd.DataFrame({"HeartDisease": np.where(data["HeartDisease"] == "Yes", 1, 0),
                           "Smoking": np.where(data["Smoking"] == "Yes", 1, 0),
                           "AlcoholDrinking": np.where(data["AlcoholDrinking"] == "Yes", 1, 0),
                           "Stroke": np.where(data["Stroke"] == "Yes", 1, 0),
                           "DiffWalking": np.where(data["DiffWalking"] == "Yes", 1, 0),
                           "Sex": np.where(data["Sex"] == "Yes", 1, 0),
                           "PhysicalActivity": np.where(data["PhysicalActivity"] == "Yes", 1, 0),
                           "KidneyDisease": np.where(data["KidneyDisease"] == "Yes", 1, 0),
                           "SkinCancer": np.where(data["SkinCancer"] == "Yes", 1, 0),
                           "Asthma": np.where(data["Asthma"] == "Yes", 1, 0)})

data_model["BMI"] = data["PhysicalHealth"]
data_model["PhysicalHealth"] = data["PhysicalHealth"]
data_model["MentalHealth"] = data["MentalHealth"]
data_model["SleepTime"] = data["SleepTime"]

# last categorical
data_model["AgeCategory"] = data["AgeCategory"]
data_model["Race"] = data["Race"]
data_model["Diabetic"] = data["Diabetic"]
data_model["GenHealth"] = data["GenHealth"]

data_model = pd.get_dummies(data_model)
 
# Creating model
y = data_model.HeartDisease
X = data_model.drop("HeartDisease", axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# test and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

# Create classifiers

# SVM
svm_clf = SGDClassifier(max_iter=1000, tol=1e-3, random_state=1, loss="huber")
log_clf = SGDClassifier(max_iter=1000, tol=1e-3, random_state=1, loss="log_loss")

# Ajustando os modelos
svm_clf.fit(X_train, y_train)
log_clf.fit(X_train, y_train)

# plotado os graficos
y_pred_svm = svm_clf.decision_function(X_test)
fpr_svm, tpr_svm, _ = metrics.roc_curve(y_test, y_pred_svm)
auc_svm = round(metrics.roc_auc_score(y_test, y_pred_svm), 4)

y_pred_log = log_clf.predict_proba(X_test)[:, 1]
fpr_log, tpr_log, _ = metrics.roc_curve(y_test, y_pred_log)
auc_log = round(metrics.roc_auc_score(y_test, y_pred_log), 4)

# Gini
gini_svm = round(2*auc_svm - 1, 4)
gini_log = round(2*auc_log - 1, 4)

# graficos
plt.plot(fpr_svm,tpr_svm,label="Support Vector Machine \nAUROC="+str(auc_svm) + "\nGini=" + str(gini_svm))
plt.plot(fpr_log,tpr_log,label="Logistic Regression \nAUROC="+str(auc_log) + "\nGini=" + str(gini_log))
plt.legend()
plt.show()

# Variaveis que influenciam

coef_svm = pd.concat([pd.DataFrame(X_train.columns),pd.DataFrame(np.transpose(svm_clf.coef_))], axis = 1)
coef_log = pd.concat([pd.DataFrame(X_train.columns),pd.DataFrame(np.transpose(log_clf.coef_))], axis = 1)

coef_svm.columns = ["Coef", "Values"]
coef_log.columns = ["Coef", "Values"]

last3_svm = coef_svm.sort_values(by="Values").head(3)
last3_log = coef_log.sort_values(by="Values").head(3)

top3_svm = coef_svm.sort_values(by="Values").tail(3)
top3_log = coef_log.sort_values(by="Values").tail(3)

# infulenciam positivamente
print(top3_svm)
print(top3_log)

print(last3_svm)
print(last3_log)

# Apendice ----
# cross_val_score(sgd_clf, X_train, y_train, cv=10, scoring="accuracy")
# y_train_pred_sgd = cross_val_predict(sgd_clf, X_train, y_train, cv = 10)
# cm_sgd = confusion_matrix(y_train, y_train_pred_sgd)

# cm_sgd / cm_sgd.astype(np.float).sum(axis=1)

# sgd_predict = sgd_clf.predict(X_test)