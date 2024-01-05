import cv2
import numpy as np

image = cv2.imread("Images/shapes.png")

# Step 1 :Convert the image to greyscale
img_greyscale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Step 2 :Cannyedge to detect edges
lower_threshold = 100
higher_threshold = 150
canny_edge = cv2.Canny(img_greyscale,lower_threshold,higher_threshold)

# Step 3 : find the contours
contours,hirearchy = cv2.findContours(canny_edge.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

# Step 4 : find the length of contours
print(f"Length of the contours = {str(len(contours))}")
for cnt in contours:
    area = cv2.contourArea(cnt)
    print("Area of eac contours:",area)

# Step 5 : Draw the contour
    img_copy = image.copy()
    cv2.drawContours(img_copy,cnt,-1,(0,255,0),3)

# Step 6 : Find the arc line of contour
    peri = cv2.arcLength(cnt,True)

# STep 7 :

cv2.imshow("drawcontours",img_copy)
cv2.waitKey(0)
