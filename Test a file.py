#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import filedialog
from tkinter import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
import joblib
import cv2,os
import numpy as np
import csv

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png *.tif"),("all files","*.*")))
print (root.filename)


# In[5]:


import cv2,os
import numpy as np
import csv
import glob
files=["B:\ML_Project\csv\\file.csv","B:\\ML_Project\\Parasites\\file2.csv"]

for file in files :
    dataframe = pd.read_csv(file,error_bad_lines=False)
    if "Parasites" in file:
        x = dataframe.drop(["type"],axis=1)
        y = dataframe["type"]
    else :
        x = dataframe.drop(["Label"],axis=1)
        y = dataframe["Label"]
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

    model = RandomForestClassifier(n_estimators=100,max_depth=4)
    model.fit(x_train,y_train)
    


    im = cv2.imread(root.filename)
    im = cv2.GaussianBlur(im,(5,5),2)
    im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(im_gray,127,255,0)
    im2,contours,_ = cv2.findContours(thresh,1,2)
    if "Parasites" in file:
        feature=np.arange(6)
        if "R" in file: 
            feature[0]=str(1)
        elif "S" in file: 
            feature[0]=str(2)
        elif "T" in file: 
            feature[0]=str(3)
        elif "G" in file: 
            feature[0]=str(4)
        else : 
            feature[0]=str(5)

        for i in range(5):
            try:
                area = cv2.contourArea(contours[i])
                j=i+1
                feature[j]=str(area)
            except:
                j=i+1
                feature[j]="0"
        prediction = model.predict([feature])
        print(prediction)

    else:
        num=len(contours)
        if "cell_images"not in root.filename:
            num=num+1
            
        if num>=5 :
            number=5
        else :
            number=num
        
        prediction = model.predict([[number]])
        print(prediction)
        if prediction[0] == 'Uninfected' :
            break
        


# In[ ]:





# In[ ]:




