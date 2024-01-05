import cv2

img = cv2.imread("Images/image.jpg")

image_resize = cv2.resize(img,(650,650))
cv2.imshow("img",image_resize)
cv2.waitKey(0)
print(image_resize.shape)