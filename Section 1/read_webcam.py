import cv2

video = cv2.VideoCapture(0)
video.set(3,640) #width
video.set(4,480) #height
video.set(10,150) #brightness
while True:
    success,frame = video.read()
    if success:
        cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()