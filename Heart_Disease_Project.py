#!/usr/bin/env python
# coding: utf-8

# In[112]:


# Heart Disease Project Gender Analysis
# Jae H. Cho
# April 9, 2019

# Import necessary libraries

import os
import pandas as pd
import numpy as np

# Plot Analysis

import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(color_codes=True)

from matplotlib import rcParams
from matplotlib.cm import rainbow

from scipy.stats import pearsonr

# df['class'].value_counts().plot('bar')


# In[113]:


#Load the heart.csv data file
pd.set_option('display.max_rows', None)
data = pd.read_csv('heart.csv')
data


# In[114]:


#Observe the first top 5 default rows of the heart disease data

data.head(5)


# In[115]:


data.tail(5)


# In[116]:


data.dtypes


# In[117]:


#Observe to see if there are any null values necessary to impute or leave out.

data.isnull().sum()


# In[118]:


data.isnull().values.any()


# In[119]:


data.isnull().sum().sum()


# In[120]:


#Display the overall structure of data (rows,columns)

data.shape


# In[121]:


data.count()


# In[122]:


duplicate_rows_data = data[data.duplicated()]
print("number of duplicate rows: ", duplicate_rows_data.shape)


# In[123]:


#We can see there are a total of 303 observations and 14 variables in the provided data set
#Lets observe some more feature statistics

data.describe()


# In[124]:


corr = data.corr()['target'].abs().sort_values()
corr


# In[181]:


sns.countplot(data.target)
plt.show()


# In[126]:


# Lets observe sex from those who have the 'target' disease and those whom do not for males and females
# Credit to Zhenhui Xie for comparison function

def sideplot(data, col, kind="bar", title = None):
    assert kind in ["bar", "hist"]
    fig = plt.figure(figsize=(10, 6))
    if kind == "bar":
        ax1 = plt.subplot(2, 2, 1)
        data[data.target == 1][['target', col]].groupby(col).count().plot(kind='bar', rot = 0, legend = False, ax = ax1, color = "r")
        ax2 = plt.subplot(2, 2, 2)
        data[data.target == 0][['target', col]].groupby(col).count().plot(kind='bar', rot = 0, legend = False, ax = ax2, color = "b")
    else:
        ax1 = plt.subplot(2, 2, 1)
        plt.hist(data[data.target == 1][col], color = "b")
        plt.xlabel(col)
        ax2 = plt.subplot(2, 2, 2)
        plt.hist(data[data.target == 0][col], color = "b")
        plt.xlabel(col)
    # Re-adjusting
    ylim = (0, max(ax1.get_ylim()[1], ax2.get_ylim()[1]))
    ax1.set_ylim(ylim)
    ax2.set_ylim(ylim)
    xlim = (min(ax1.get_xlim()[0], ax2.get_xlim()[0]), max(ax1.get_xlim()[1], ax2.get_xlim()[1]))
    ax1.set_xlim(xlim)
    ax2.set_xlim(xlim)
    if title is not None:
        fig.suptitle(title)


# In[127]:


sideplot(data, "chol", kind = "hist", title = "Comparison of serum cholestoral")


# In[128]:


#For the variable sex(1 = male; 0 = female)

sideplot(data, "sex", kind = "bar", title = "Comparison by Sex")
plt.show()


# In[129]:


# data['sex'][data['sex'] == 0] = 'female'
# data['sex'][data['sex'] == 1] = 'male'
# It seems there are more males than females in both cases of those who don't have heart disease and those that do 
# have heart disease. 


# In[130]:


data.sample()


# In[131]:


total_genders_count=len(data.sex)
male_count=len(data[data['sex']==1])
female_count=len(data[data['sex']==0])
print('Total Genders :',total_genders_count)
print('Male Count    :',male_count)
print('Female Count  :',female_count)


# In[132]:


#Lets now separate the data into males and females
female_data = data[data['sex'] == False]
male_data = data[data['sex'] == True]


# In[133]:


female_data


# In[134]:


male_data


# In[135]:


# Let's create a separate list of values for categorical versus quantitative data.

categorical_val = []             # categorical data
continous_val = []               # quantitative data

for column in data.columns:
    print('==============================')
    print(f"{column} : {data[column].unique()}")
    if len(data[column].unique()) <= 10:
        categorical_val.append(column)
    else:
        continous_val.append(column)


# In[136]:


# Let's view our categorical values.

categorical_val


# In[137]:


# After carefully observing the data, I found that it was neccessary to change some categorical variables to 
# dummy variables and scale all the values before training the Machine Learning models. First, I'll use the command
# "get_dummies," to create dummy columns for the categorical variables.


# In[138]:


categorical_val.remove('target')


# In[139]:


# categorical_val.remove('target')
# dataset = pd.get_dummies(df, columns = categorical_val)
# from sklearn.model_selection import train_test_split

# X = dataset.drop('target', axis=1)
# y = dataset.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# In[140]:


dataset = pd.get_dummies(data, columns = categorical_val)


# In[141]:


from sklearn.preprocessing import StandardScaler

s_sc = StandardScaler()
col_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
dataset[col_to_scale] = s_sc.fit_transform(dataset[col_to_scale])


# In[142]:


from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

def print_score(clf, X_train, y_train, X_test, y_test, train=True):
    if train:
        pred = clf.predict(X_train)
        print("Train Result:\n================================================")
        print(f"Accuracy Score: {accuracy_score(y_train, pred) * 100:.2f}%")
        print("_______________________________________________")
        print("Classification Report:", end='')
        print(f"\tPrecision Score: {precision_score(y_train, pred) * 100:.2f}%")
        print(f"\t\t\tRecall Score: {recall_score(y_train, pred) * 100:.2f}%")
        print(f"\t\t\tF1 score: {f1_score(y_train, pred) * 100:.2f}%")
        print("_______________________________________________")
        print(f"Confusion Matrix: \n {confusion_matrix(y_train, pred)}\n")
        
    elif train==False:
        pred = clf.predict(X_test)
        print("Test Result:\n================================================")        
        print(f"Accuracy Score: {accuracy_score(y_test, pred) * 100:.2f}%")
        print("_______________________________________________")
        print("Classification Report:", end='')
        print(f"\tPrecision Score: {precision_score(y_test, pred) * 100:.2f}%")
        print(f"\t\t\tRecall Score: {recall_score(y_test, pred) * 100:.2f}%")
        print(f"\t\t\tF1 score: {f1_score(y_test, pred) * 100:.2f}%")
        print("_______________________________________________")
        print(f"Confusion Matrix: \n {confusion_matrix(y_test, pred)}\n")


# In[143]:


from sklearn.model_selection import train_test_split

X = dataset.drop('target', axis=1)
y = dataset.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# In[144]:


from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression(solver='liblinear')
log_reg.fit(X_train, y_train)


# In[145]:


print_score(log_reg, X_train, y_train, X_test, y_test, train=True)
print_score(log_reg, X_train, y_train, X_test, y_test, train=False)


# In[146]:


test_score = accuracy_score(y_test, log_reg.predict(X_test)) * 100
train_score = accuracy_score(y_train, log_reg.predict(X_train)) * 100

data_results = pd.DataFrame(data=[["Logistic Regression", train_score, test_score]], 
                          columns=['Model', 'Training Accuracy %', 'Testing Accuracy %'])
data_results


# In[147]:


from sklearn.svm import SVC


svm_model = SVC(kernel='rbf', gamma=0.1, C=1.0)
svm_model.fit(X_train, y_train)


# In[148]:


print_score(svm_model, X_train, y_train, X_test, y_test, train=True)
print_score(svm_model, X_train, y_train, X_test, y_test, train=False)


# In[149]:


test_score = accuracy_score(y_test, svm_model.predict(X_test)) * 100
train_score = accuracy_score(y_train, svm_model.predict(X_train)) * 100

results_df_2 = pd.DataFrame(data=[["Support Vector Machine", train_score, test_score]], 
                          columns=['Model', 'Training Accuracy %', 'Testing Accuracy %'])
results_df = data_results.append(results_df_2, ignore_index=True)
results_df


# In[180]:


#knn

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
knn_val = []
# for k in range (1,21):
    # knn_classifier = KNeighborsClassifier(n_neighbors = k)
    # score = cross_val_score(knn_classifier,X,y,cv=12)
    # knn_val.append(score.mean())

knn_classifier = KNeighborsClassifier(n_neighbors = 12)
score = cross_val_score(knn_classifier,X,y,cv=10)
score.mean()


# In[ ]:


from sklearn.ensemble import RandomForestClassifier


# In[151]:


rfc = RandomForestClassifier(n_estimators=12)
score = cross_val_score(rfc, X, y, cv=12)


# In[152]:


score.mean()


# In[184]:


g = sns.FacetGrid(data, col='target')
g.map(plt.hist, 'age', bins=10)

g2 = sns.FacetGrid(data, col='target')
g2.map(plt.hist, 'trestbps', bins=10, color = "green")

g3 = sns.FacetGrid(data, col='target')
g3.map(plt.hist, 'chol', bins=10, color = "skyblue")

g4 = sns.FacetGrid(data, col='target')
g4.map(plt.hist, 'thalach', bins=10, color = "coral")

g5 = sns.FacetGrid(data, col='target')
g5.map(plt.hist, 'sex', bins=10, color = "gray")

g5 = sns.FacetGrid(data, col='target')
g5.map(plt.hist, 'oldpeak', bins=10, color = "pink")


# In[154]:


grid = sns.FacetGrid(data, col='target', row='sex', height=3.2, aspect=1.8)
grid.map(plt.hist, 'age', alpha=.5, bins=20)
grid.add_legend();


# In[155]:


corr, _ = pearsonr(data['age'], data['chol'])
print('Pearsons correlation for age and chol: %.3f' % corr)

corr, _ = pearsonr(data['age'], data['trestbps'])
print('Pearsons correlation for trestbps and age: %.3f' % corr)

corr, _ = pearsonr(data['trestbps'], data['chol'])
print('Pearsons correlation for trestbps and chol: %.3f' % corr)

corr, _ = pearsonr(data['thalach'], data['oldpeak'])
print('Pearsons correlation for thalach and oldpeak: %.3f' % corr)


# In[175]:


data.hist(column='age', bins=25, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)


# In[176]:


#fig = plt.figure(figsize = (15,20))
#ax = fig.gca()
#data.hist(ax = ax)


# In[ ]:




