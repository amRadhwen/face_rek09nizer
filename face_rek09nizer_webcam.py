# import opencv
import cv2 as cv

# import numpy
import numpy as np

# import facerecognition
import face_recognition as fr

# define vi capture object

video = cv.VideoCapture(0)

if not video.isOpened():
    print("Cannot open webcam !")
    exit()

# capture loop
counter = 0
while True:
    # capture video frame by frame
    ret, frame = video.read()

    if not ret:
        print("Cannot receive frames, something is wrong !")
        exit()

    # display the resulting frame
    cv.imshow("frame", frame)
    
    # convet frame from BGR used by openCV to RGB wich is used by face recognition
    rgb_frame = frame[:, :, ::-1]
    


    # define capture quit button (in this case it's the 'q' button)
    if cv.waitKey(0) == ord('q'):
        break

    # define photo capture key (in this case
    if cv.waitKey(0) == ord('c'):
        cv.imwrite('rek09nizer'+str(counter)+".png", frame)

    counter += 1

# release the capture object after exit the loop
video.release()

# destroy the window
cv.destroyAllWindows()