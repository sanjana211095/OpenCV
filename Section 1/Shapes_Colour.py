import cv2
import numpy as np

#blank image
img = np.zeros((512,512,3))

#Add colour
img[:] = 45,90,0

#Draw a line
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)


#Draw a rectangle
cv2.rectangle(img,(0,0),(250,250),(0,255,0),4)

#Draw a circle
cv2.circle(img,(400,50),30,(0,255,0),4)

#Write text on image
cv2.putText(img,"Open Cv",(300,200),cv2.FONT_ITALIC,1,(0,255,34),5)
cv2.imshow("something",img)
cv2.waitKey(0)
