
# coding: utf-8

# In[46]:


#Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[47]:


data = pd.read_csv("L1Data.csv")


# In[48]:


data


# In[49]:


X = data[["Class", "Age", "Funds"]].values


# In[50]:


X[1][0]


# In[51]:


y = data[["Sale"]].values


# In[52]:


y


# In[53]:


X


# In[54]:


from sklearn.preprocessing import Imputer


# In[55]:


imputing_configuration = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)


# In[56]:


imputed_values = imputing_configuration.fit(X[:,[1,2]])


# In[57]:


X[:,[1,2]] = imputed_values.transform(X[:,[1,2]])


# In[58]:


X


# In[59]:


from sklearn.preprocessing import LabelEncoder


# In[60]:


discreteCoder_X = LabelEncoder()
X[:,0] = discreteCoder_X.fit_transform(X[:,0])


# In[61]:


X


# In[62]:


from sklearn.preprocessing import OneHotEncoder


# In[63]:


discreteCoder_X_dummies = OneHotEncoder(categorical_features = [0])
X = discreteCoder_X_dummies.fit_transform(X).toarray() 


# In[64]:


X


# In[65]:


discreteCoder_y = LabelEncoder()
y = discreteCoder_y.fit_transform(y)


# In[66]:


y


# In[67]:


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 1693)


# In[68]:


X_train


# In[69]:


X_test


# In[70]:


y_train


# In[71]:


y_test


# In[72]:


from sklearn.preprocessing import StandardScaler

scale_X = StandardScaler()
X_train = scale_X.fit_transform(X_train)
X_test = scale_X.transform(X_test)


# In[73]:


X_test

