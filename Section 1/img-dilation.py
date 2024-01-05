import cv2
import numpy as np

img = cv2.imread("Images/documentscanner2.jpg")
kernel = np.ones((5,5),np.uint8)
#setting threshold value
lower = 100
higher = 120

#Apply Cannyedge
img_canny = cv2.Canny(img,lower,higher)

#Dilation
imgdilation = cv2.dilate(img_canny,kernel,iterations=1)
cv2.imshow("img",imgdilation)
cv2.waitKey(0)

