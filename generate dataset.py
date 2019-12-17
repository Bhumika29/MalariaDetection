#!/usr/bin/env python
# coding: utf-8

# In[24]:


import cv2,os
import numpy as np
import csv
import glob

labels = ['Parasitized','Uninfected']

file = open("B:\ML_Project\csv\\file.csv","a")


# In[26]:


for label in labels :
	dirList = glob.glob("B:\\ML_Project\\cell_images\\"+label+"\\*.png")
	for img_path in dirList:

		im = cv2.imread(img_path)

		im = cv2.GaussianBlur(im,(5,5),2)



		im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

		ret,thresh = cv2.threshold(im_gray,127,255,0)
		im2,contours,_ = cv2.findContours(thresh,1,2)

		file.write(label)
		file.write(",")

		for i in range(5):
			try:
				area = cv2.contourArea(contours[i])
				file.write(str(area))
			except:
				file.write("0")

			file.write(",")


		file.write("\n")


cv2.waitKey(19000)

file.close();


# In[27]:


file


# In[ ]:





# In[ ]:




