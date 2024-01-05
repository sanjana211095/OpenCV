import cv2

img = cv2.imread("Images/documentscanner2.jpg")
#setting threshold value
lower = 100
higher = 120

#Apply Cannyedge
img_canny = cv2.Canny(img,lower,higher)
cv2.imshow("img",img_canny)
cv2.waitKey(0)
