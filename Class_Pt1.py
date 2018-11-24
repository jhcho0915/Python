
# coding: utf-8

# In[129]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("./data.csv")


# In[130]:


data


# In[131]:


list(data)


# In[132]:


data
data.shape


# In[133]:


X = data.iloc[:,2:4]
y = data.iloc[:,1]
X = X.values
y = y.values
X


# In[134]:


y


# In[135]:


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=1693)
scale_X = StandardScaler()
X_train = scale_X.fit_transform(X_train)
X_test = scale_X.transform(X_test)


# In[136]:


from sklearn.linear_model import LogisticRegression


# In[137]:


logistic_classifier = LogisticRegression(random_state=1693)


# In[138]:


logistic_classifier.fit(X_train, y_train)


# In[139]:


y_pred = logistic_classifier.predict(X_test)


# In[140]:


y_pred


# In[141]:


y_test


# In[142]:


y_pred_probabilities = logistic_classifier.predict_proba(X_test)


# In[143]:


y_pred_probabilities


# In[144]:


log_tumorA = [[15.78, 17.89]]
log_tumorA

log_tumor_scaledA = scale_X.transform(log_tumorA)
logtumorA_prediction = logistic_classifier.predict_proba(log_tumor_scaledA)

logtumorA_prediction


# In[145]:


from sklearn.metrics import confusion_matrix


# In[146]:


confMat = confusion_matrix(y_test, y_pred)
confMat


# In[147]:


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


# In[148]:


print_cm(confMat, ["Benign", "Malignant"])


# In[149]:


from sklearn.neighbors import KNeighborsClassifier


# In[150]:


nn_classifier = KNeighborsClassifier(n_neighbors = 5, metric="minkowski",p=2)


# In[151]:


nn_classifier.fit(X_train, y_train)


# In[152]:


y_pred_NN = nn_classifier.predict(X_test)


# In[153]:


y_pred_NN


# In[154]:


y_test


# In[155]:


nn_tumorA = [[17.18, 8.65]]
nn_tumorA

nn_tumor_scaledA = scale_X.transform(nn_tumorA)
nntumorA_prediction = nn_classifier.predict(nn_tumor_scaledA)

nntumorA_prediction


# In[156]:


confMat_NN = confusion_matrix(y_test, y_pred_NN)
print_cm(confMat_NN, ["Benign", "Malignant"])


# In[157]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import LabelEncoder

def viz_cm(model, labels):

    X_set, y_set = X_test, y_test
    X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                         np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))

    pred = model.predict(np.array([X1.ravel(), X2.ravel()]).T)

    discreteCoder = LabelEncoder()
    pred = discreteCoder.fit_transform(pred)

    plt.contourf(X1, X2, pred.reshape(X1.shape),
                 alpha = 0.75, cmap = ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                    c = ListedColormap(('red', 'green'))(i), label = j)
    plt.title('Classification')
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.legend()
    plt.show()


# In[158]:


viz_cm(model=nn_classifier, labels=["Radius Mean", "Texture Mean"])


# In[159]:


from sklearn.svm import SVC
svc_classifier = SVC(kernel="linear", random_state=1693)
svc_classifier.fit(X_train, y_train)


# In[160]:


y_pred_SVC = svc_classifier.predict(X_test)


# In[161]:


y_pred_SVC


# In[162]:


confMat_SVC = confusion_matrix(y_test, y_pred_SVC)
print_cm(confMat_SVC, ["Benign", "Malignant"])


# In[163]:


viz_cm(model = svc_classifier, labels=["Radius Mean", "Texture Mean"])


# In[164]:


from sklearn.svm import SVC
kernelSVC_classifier = SVC(kernel="rbf", random_state=1693)
kernelSVC_classifier.fit(X_train, y_train)


# In[165]:


y_pred_SVC_kernel = kernelSVC_classifier.predict(X_test)


# In[166]:


y_pred_SVC_kernel


# In[167]:


kernelSVC_tumorA = [[15.78, 17.89]]
kernelSVC_tumorA

kernelSVC_tumor_scaledA = scale_X.transform(kernelSVC_tumorA)
kernelSVCtumorA_prediction = kernelSVC_classifier.predict(kernelSVC_tumor_scaledA)

kernelSVCtumorA_prediction


# In[168]:


confMat_SVC_kernel = confusion_matrix(y_test, y_pred_SVC_kernel)
print_cm(confMat_SVC_kernel, ["Benign", "Malignant"])


# In[169]:


viz_cm(model = kernelSVC_classifier, labels = ["Radius Mean", "Texture Mean"])

