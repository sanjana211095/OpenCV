import cv2

img = cv2.imread("Images/lambo.png")
img_cropped = img[0:200,200:500] #height,width
cv2.imshow("image",img_cropped)
cv2.waitKey(0)
