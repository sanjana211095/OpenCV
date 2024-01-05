import cv2
import numpy as np

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")


while True:
    ret, frame = cap.read()
    if ret:
        grey_scale_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face = faceCascade.detectMultiScale(grey_scale_frame,1.1,4)
        for x,y,w,h in face:
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,12,56),3) 
        cv2.imshow("Output stream",frame)
        if cv2.waitKey(1) & 0xFF==ord('1'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
