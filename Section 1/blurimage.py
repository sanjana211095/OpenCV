import cv2

image = cv2.imread("Images/cards.jpg")
imgblur = cv2.GaussianBlur(image,(27,27),0)  # kernelsize increase = blur increases.it should be odd number.

cv2.imshow("img",imgblur)
cv2.waitKey(0)