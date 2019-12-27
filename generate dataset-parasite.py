#!/usr/bin/env python
# coding: utf-8

# In[12]:


import cv2,os
import numpy as np
import csv
import glob
types=['Falciparum','Vivax']

file = open("B:\\ML_Project\\Parasites\\file2.csv","a")


# In[13]:


for t in types :
    dirList = glob.glob("B:\\ML_Project\\Parasites\\"+t+"\\*.tif")
    for img_path in dirList:

        im = cv2.imread(img_path)

        im = cv2.GaussianBlur(im,(5,5),2)


        im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        ret,thresh = cv2.threshold(im_gray,127,255,0)
        im2,contours,_ = cv2.findContours(thresh,1,2)

        file.write(t)
        file.write(",")
        if "R" in img_path: 
            file.write(str(1))
            file.write(",")
        elif "S" in img_path: 
            file.write(str(2))
            file.write(",")
        elif "T" in img_path: 
            file.write(str(3))
            file.write(",")
        elif "G" in img_path: 
            file.write(str(4))
            file.write(",")
        else : 
            file.write(str(5))
            file.write(",")

        for i in range(5):
            try:
                area = cv2.contourArea(contours[i])
                print(area)
                file.write(str(area))
            except:
                file.write("0")

            file.write(",")


        file.write("\n")


cv2.waitKey(19000)
file.close();


# In[27]:


file


# In[12]:


dirList


# In[10]:


file


# In[ ]:




