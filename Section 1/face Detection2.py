import cv2
import numpy as np

image = cv2.imread("Images/face.png")
faceCascade = cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")

grey_scale_frame = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
face = faceCascade.detectMultiScale(grey_scale_frame,1.1,4)
for x,y,w,h in face:
   cv2.rectangle(image,(x,y),(x+w,y+h),(255,12,56),3)
cv2.imshow("Output stream",image)
cv2.waitKey(0)