
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

students_math = pd.read_csv("./studentmat.csv")
students_port = pd.read_csv("./studentpor.csv")


# In[24]:


students_port.shape


# In[25]:


all_student_rows = [students_math, students_port]


# In[26]:


all_students = pd.concat(all_student_rows, ignore_index=True)


# In[27]:


all_students.shape


# In[28]:


all_students
X = all_students[["age", "address", "traveltime", "failures", "higher", 
                  "internet", "romantic", "famrel", "freetime", "goout", "absences"]].values

from sklearn.preprocessing import LabelEncoder
discreteCoder_X = LabelEncoder()


# In[29]:


X


# In[30]:


X[:,1] = discreteCoder_X.fit_transform(X[:,1])
X[:,4] = discreteCoder_X.fit_transform(X[:,4])
X[:,5] = discreteCoder_X.fit_transform(X[:,5])
X[:,6] = discreteCoder_X.fit_transform(X[:,6])


# In[31]:


X[:,1]


# In[32]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

y = all_students[["Walc"]].values


# In[33]:


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=1693)


# In[34]:


scale_X = StandardScaler()
X_train = scale_X.fit_transform(X_train)
X_test = scale_X.transform(X_test)


# In[35]:


from sklearn.svm import SVR


# In[36]:


svr_regression = SVR(kernel = "linear", epsilon = 1.0)
svr_regression.fit(X_train, y_train)


# In[37]:


#Student A
#Age: 18
#Address: Urban (Label encoded as 1)
#Travel Time: 3 (30 minutes to 1 hour)
#Failures: 3
#Desire for Higher Education: No (0)
#Internet Access: No (0)
#Romantic Relationship: Yes (1)
#Relationship with Family: Ok (2 out of 5)
#Freetime: A lot (5 out of 5)
#Going Out: A bit (2 out of 5)
#Absences: 5

new_studentA = [[18, 1, 3, 3, 0, 0, 1, 2, 5, 2, 5]]


# In[38]:


new_studentA


# In[39]:


new_student_scaledA = scale_X.transform(new_studentA)
studentA_prediction = svr_regression.predict(new_student_scaledA)


# In[40]:


studentA_prediction


# In[41]:


print("First new student (A):" + str(studentA_prediction))


# In[42]:


#Student B
#Age: 18
#Address: Rural (Label encoded as 0)
#Travel Time: 3 (30 minutes to 1 hour)
#Failures: 3
#Desire for Higher Education: No (0)
#Internet Access: No (0)
#Romantic Relationship: Yes (1)
#Relationship with Family: Ok (2 out of 5)
#Freetime: Very little (1 out of 5)
#Going Out: Very little (1 out of 5)
#Absences: 5

new_studentB = [[18, 0, 3, 3, 0, 0, 1, 2, 1, 1, 5]]
new_student_scaledB = scale_X.transform(new_studentB)
studentB_prediction = svr_regression.predict(new_student_scaledB)
print("Second new student:" + str(studentB_prediction))


# In[43]:


new_studentC = [[20, 1, 3, 1, 0, 1, 1, 2, 3, 2, 5]]
new_student_scaledC = scale_X.transform(new_studentC)
studentC_prediction = svr_regression.predict(new_student_scaledC)
print("Third new student:" + str(studentC_prediction))


# In[44]:


from sklearn import tree


# In[45]:


DT_regression = tree.DecisionTreeRegressor(random_state=1693, max_depth=3)
DT_regression.fit(X_train, y_train)


# In[46]:


tree.export_graphviz(DT_regression, out_file="tree.dot", feature_names =["age", "address",
                                                                        "traveltime", "failures", "higher", 
                                                                        "internet", "romantic", "famrel", 
                                                                        "freetime", "goout", "absences"])


# In[47]:


studentA_prediction_RT = DT_regression.predict(new_student_scaledA)
print("First new student (A):" + str(studentA_prediction_RT))


# In[48]:


studentB_prediction_RT = DT_regression.predict(new_student_scaledB)
print("Second new student (B):" + str(studentB_prediction_RT))


# In[49]:


from sklearn.ensemble import RandomForestRegressor
RF_regression = RandomForestRegressor(n_estimators = 100, random_state=1693)
RF_regression.fit(X_train, y_train)


# In[50]:


studentA_prediction_RF = RF_regression.predict(new_student_scaledA)
print("First new student:" + str(studentA_prediction_RF))


# In[51]:


studentB_prediction_RF = RF_regression.predict(new_student_scaledB)
print("Second new student:" + str(studentB_prediction_RF))


# In[53]:


studentC_prediction_RF = RF_regression.predict(new_student_scaledC)
print("Third new student:" + str(studentC_prediction_RF))


# In[56]:


from sklearn.metrics import mean_absolute_error
rf_MAD = mean_absolute_error(y_test, RF_regression.predict(X_test))


# In[57]:


rf_MAD


# In[59]:


RT_MAD = mean_absolute_error(y_test, DT_regression.predict(X_test))
SVR_MAD = mean_absolute_error(y_test, svr_regression.predict(X_test))


# In[60]:


print("Random Forest MAD: " + str(rf_MAD))
print("Random Tree MAD MAD: " + str(RT_MAD))
print("Support VEctor Regression MAD: " + str(SVR_MAD))

