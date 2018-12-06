
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# In[2]:


ccdb = pd.read_csv("UCI_Credit_Card.csv")


# In[3]:


ccdb.head()


# In[4]:


ccdb.describe().transpose()


# In[5]:


X = ccdb.drop("default.payment.next.month", axis=1)


# In[6]:


y = ccdb["default.payment.next.month"]


# In[7]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1693)


# In[8]:


scale_X = StandardScaler()
X_train = scale_X.fit_transform(X_train)
X_test = scale_X.transform(X_test)


# In[19]:


X_train, y_train


# In[9]:


from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

mlp = MLPClassifier(hidden_layer_sizes=(13,13,13), max_iter=500)


# In[10]:


mlp.fit(X_train, y_train)
pred = mlp.predict(X_test)
pred


# In[11]:


nn_cm = confusion_matrix(y_test, pred)


# In[12]:


nn_cm


# In[13]:


def print_cm(cm, labels, hide_zeroes=False, hide_diagonal=False, hide_threshold=None):
    """pretty print for confusion matrixes"""
    columnwidth = max([len(x) for x in labels] + [5])  # 5 is value length
    empty_cell = " " * columnwidth
    # Print header
    print("    " + empty_cell, end=" ")
    for label in labels:
        print("%{0}s".format(columnwidth) % label, end=" ")
    print()
    # Print rows
    for i, label1 in enumerate(labels):
        print("    %{0}s".format(columnwidth) % label1, end=" ")
        for j in range(len(labels)):
            cell = "%{0}.1f".format(columnwidth) % cm[i, j]
            if hide_zeroes:
                cell = cell if float(cm[i, j]) != 0 else empty_cell
            if hide_diagonal:
                cell = cell if i != j else empty_cell
            if hide_threshold:
                cell = cell if cm[i, j] > hide_threshold else empty_cell
            print(cell, end=" ")
        print()


# In[14]:


print_cm(nn_cm, ["No Default", "Default"])


# In[15]:


updated_mlp = MLPClassifier(hidden_layer_sizes=(10,20,10),
                            activation='tanh',
                            solver = "sgd",
                            batch_size=200,
                            learning_rate="adaptive",
                            max_iter = 500,
                            verbose = True)

updated_mlp.fit(X_train, y_train)


# In[16]:


pred = updated_mlp.predict(X_test)
nn_cm = confusion_matrix(y_test, pred)
print_cm(nn_cm, ["No Default", "Default"])

