#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn import metrics
import joblib


# In[9]:


##Step1: Load Dataset

dataframe = pd.read_csv("B:\ML_Project\csv\\file.csv",error_bad_lines=False)


#Step2: Split into training and test data
x = dataframe.drop(["Label"],axis=1)
y = dataframe["Label"]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

##Step4: Build a model

model = RandomForestClassifier(n_estimators=100,max_depth=4)
model.fit(x_train,y_train)



##Step5: Make predictions and get classification report

predictions = model.predict(x_test)

print(metrics.classification_report(predictions,y_test))
print(model.score(x_test,y_test))


# In[ ]:




