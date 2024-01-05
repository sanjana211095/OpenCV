import cv2

image = cv2.imread("Images\lambo.png")
imghsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
lower = (0,103,155)
higher = (20,255,255)

mask =cv2.inRange(imghsv,lower,higher)

color_image = cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("Color Detection",color_image)
cv2.waitKey(0)