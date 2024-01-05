import cv2

image = cv2.imread("Images/cards.jpg")
imggrey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("img",imggrey)
cv2.waitKey(0)