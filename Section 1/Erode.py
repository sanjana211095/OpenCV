import cv2
import numpy as np

img = cv2.imread("Images/documentscanner2.jpg")
kernel = np.ones((5,5),np.uint8)
#setting threshold value
lower = 100
higher = 120

#Apply Cannyedge
img_canny = cv2.Canny(img,lower,higher)

#Dilation - increase the size of edges
imgdilation = cv2.dilate(img_canny,kernel,iterations=1)

imgerode = cv2.erode(imgdilation,kernel,iterations=1)
cv2.imshow("img",imgerode)
cv2.waitKey(0)


