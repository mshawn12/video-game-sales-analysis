#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import hvplot.pandas
from pathlib import Path
from sklearn.model_selection import train_test_split


# In[3]:


data = Path('./resources/video_game_cleaned.csv')
df = pd.read_csv(data)
df.head()


# In[4]:


y = df["g_sales"]
y.value_counts()


# In[5]:


X = df.drop(columns = ["g_sales", "uniqueid", "name", "yearreleased", "genre", "publisher", "developer", "rating", "nasales", "eusales", "jpsales", "othersales", "globalsales"])
X


# In[6]:


## Split our data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X,
                                                   y,
                                                   random_state =1,
                                                   stratify = y)

#y_train.value_counts()
y_test.value_counts()


# In[7]:


## Create a Logistic Regression Model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='lbfgs',
                                max_iter=200,
                                random_state=1)
model


# In[8]:


model.fit(X_train, y_train)


# In[9]:


## Score the model using the test data
print(f"Training Data Score: {model.score(X_train, y_train)}")
print(f"Testing Data Score: {model.score(X_test, y_test)}")


# In[10]:


predictions = model.predict(X_test)
results = pd.DataFrame({"Prediction": predictions, "Actual": y_test}).reset_index(drop=True)
results


# In[11]:


# Calculate the Accuracy Score
from sklearn.metrics import accuracy_score
# Display the accuracy score for the test dataset.
accuracy_score(y_test, predictions)


# In[12]:


from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, predictions)


# In[13]:


from sklearn.metrics import classification_report
#Logistic Regression
target_names = ['low', 'high']
predictions = model.predict(X_test)
print(classification_report(y_test, predictions,
                            target_names=target_names))


# In[18]:


#Support Vector Machine
from sklearn.svm import SVC
model_2 = SVC(kernel='linear')
model_2.fit(X_train, y_train)


# In[15]:


model_2.score(X_test, y_test)


# In[16]:


# Calculate the classification report
from sklearn.metrics import classification_report
#Support Vector Machine
target_names = ['low', 'high']
predictions = model_2.predict(X_test)
print(classification_report(y_test, predictions,
                            target_names=target_names))


# In[22]:


#Decision Tree Model
from sklearn import tree
from sklearn.preprocessing import StandardScaler

# Creating the decision tree classifier instance
model_3 = tree.DecisionTreeClassifier()

# Fitting the model
model_3 = model_3.fit(X_train, y_train)

# Making predictions using the testing data
predictions = model_3.predict(X_test)

# Classification Report
#Decision Tree Model
predictions = model_3.predict(X_test)
print(classification_report(y_test, predictions,
                            target_names=target_names))

