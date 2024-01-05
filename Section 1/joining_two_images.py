import cv2
import numpy as np

img1 = cv2.imread("Images/cards.jpg")

img2 = cv2.imread("Images/cards2.jpg")
img3 = cv2.resize(img2,(477,500))

print(img1.shape)
print(img2.shape)

image = np.hstack((img1,img3))  #vstack,hstack
cv2.imshow("newimage",image)
cv2.waitKey(0)
