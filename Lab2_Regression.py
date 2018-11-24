
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

piazza_data = pd.read_csv("./L2Data.csv")


# In[4]:


piazza_data


# In[5]:


X = piazza_data[["contributions"]].values
y = piazza_data[["Grade"]].values


# In[6]:


X
y


# In[7]:


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=1693)


# In[10]:


from sklearn.linear_model import LinearRegression


# In[11]:


regression = LinearRegression()
regression.fit(X_train, y_train)


# In[12]:


plt.scatter(X_train, y_train)
plt.show()


# In[13]:


plt.scatter(X_train, y_train, color = "black")
plt.plot(X_train, regression.predict(X_train), color = "red")
plt.show()


# In[15]:


plt.scatter(X_train, y_train, color = "black")
plt.plot(X_train, regression.predict(X_train), color = "red")
plt.title("Piazza contributions and Grades (Training Data)")
plt.xlabel("Piazza contributions")
plt.ylabe1("Grade")
plt.show()


# In[16]:


X_test


# In[17]:


y_predictions = regression.predict(X_test)


# In[18]:


y_predictions


# In[19]:


[y_test, y_predictions]


# In[20]:


plt.scatter(X_train, y_train, color="black")
plt.scatter(X_test, y_test, color = "blue")
plt.plot(X_train, regression.predict(X_train), color="red")
plt.title("Piazza contributions and Grades")
plt.xlabel("Piazza contributions")
plt.ylabel("Grade")
plt.show()


# In[21]:


piazza_data


# In[22]:


X = piazza_data[["contributions", "days online", "views", "questions", "answers"]].values
y = piazza_data[["Grade"]].values


# In[24]:


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.25, random_state = 1693)


# In[25]:


X_train


# In[26]:


scale_X = StandardScaler()
X_train_scaled = scale_X.fit_transform(X_train)
X_test_scaled = scale_X.transform(X_test)


# In[27]:


multiple_regression = LinearRegression()
multiple_regression.fit(X_train_scaled, y_train)


# In[30]:


y_predictions = multiple_regression.predict(X_test_scaled)


# In[31]:


[y_test, y_predictions]


# In[32]:


from sklearn.preprocessing import PolynomialFeatures


# In[33]:


X = piazza_data[["contributions", "days online", "views", "questions", "answers"]].values
y = piazza_data[["Grade"]].values


# In[36]:


poly_data = PolynomialFeatures(degree = 2)

X_poly = poly_data.fit_transform(X)


# In[37]:


X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.25, random_state=1693)


# In[38]:


X_poly


# In[39]:


poly_reg = LinearRegression()
poly_reg.fit(X_train, y_train)


# In[43]:


y_predictions = poly_reg.predict(X_test)


# In[44]:


y_predictions


# In[45]:


X = piazza_data[["contributions"]].values
y = piazza_data[["Grade"]].values

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=1693)

scale_X = StandardScaler()
X_train = scale_X.fit_transform(X_train)
X_test=scale_X.transform(X_test)


# In[46]:


lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

poly_data = PolynomialFeatures(degree=2)
poly_reg = LinearRegression()
poly_reg.fit(poly_data.fit_transform(X_train), y_train)


# In[47]:


plt.scatter(X_test, y_test, color = "black", label = "Truth")
plt.scatter(X_test, lin_reg.predict(X_test), color="green", label="Linear")
plt.scatter(X_test, poly_reg.predict(poly_data.fit_transform(X_test)), color="blue", label="Poly")
plt.xlabel("Piazza Contributions")
plt.ylabel("Grade")
plt.legend()
plt.show()

