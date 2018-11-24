
# coding: utf-8

# In[1]:


import pandas as pd
dta = pd.read_csv('dailyinmatesincustody.csv')
dta = dta.dropna(subset=["GENDER"])
X = dta[["AGE", "GENDER"]]
y = dta["INFRACTION"]
X = pd.get_dummies(X)
X = X.drop(columns=["GENDER_M"])
y = pd.get_dummies(y)
y = y.drop(columns=["N"])

X = X.values
y = y.values


# In[2]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

dt_classifier = DecisionTreeClassifier(random_state=1693, max_depth=2, min_samples_leaf = 2)
dt_classifier.fit(X,y)
k_fold = cross_val_score(estimator = dt_classifier, X=X, y=y, cv=10, scoring="accuracy")
k_fold.mean()


# In[6]:


from sklearn.model_selection import GridSearchCV

params = [{'max_depth':[1,2,3,4,5], 'min_samples_leaf':[2,4,6,8,10,12,14,16,18,20]}]

gSearch = GridSearchCV(estimator = dt_classifier,
                       param_grid = params,
                       scoring = 'accuracy',
                       cv = 5)


# In[7]:


gSearch_results = gSearch.fit(X,y)


# In[9]:


gSearch_results


# In[10]:


gSearch_results.best_params_


# In[7]:


gSearch_results.best_score_

