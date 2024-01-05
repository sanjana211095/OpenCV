import cv2
import numpy as np

cap =cv2.VideoCapture("Videos/demo.mp4")
NumberPlateCascade = cv2.CascadeClassifier("haarcascades/haarcascade_russian_plate_number.xml")

count =0
while True:
    ret,frame =cap.read()
    if ret:
        print("Frame Shape",frame.shape)
        frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        number_plate = NumberPlateCascade.detectMultiScale(frame_gray,1.1,10)
        for x,y,w,h in number_plate:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),3)
            cv2.putText(frame,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),3)
            frameROI = frame[y:y+h,x:x+w]
        cv2.imshow("Frame ROI",frameROI)
        cv2.imshow("Output video",frame)
        if cv2.waitKey(1) & 0xFF==ord('1'):
            cv2.imwrite("Resources/Noplate"+str(count)+".jpg",frameROI)
            cv2.rectangle(frame,(0,200),(640,300),(0,255,0),cv2.FILLED)
            cv2.putText(frame,"Scan Saved",(150,265),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(245,0,123),2)
            cv2.imshow("Output video", frame)
            cv2.waitKey(500)
            count+=1
            
    else:
        break