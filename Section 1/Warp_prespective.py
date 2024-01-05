import cv2
import numpy as np

img = cv2.imread("Images/cards.jpg")

width,heigth = 500,500
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,heigth],[width,heigth]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgoutput = cv2.warpPerspective(img,matrix,(width,heigth))
cv2.imshow("Original",imgoutput)
cv2.waitKey(0)
