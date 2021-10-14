# import opencv
import cv2

# define vi capture object

video = cv2.VideoCapture(0);

# capture loop

while True:
    # capture video frame by frame
    ret, frame = video.read()

    # display the resulting frame
    cv2.imshow("frame", frame)

    # define capture quit button (in this case th 'q' button)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

# release the capture object after exit the loop
video.release()

# destroy the window
cv2.destroyWindow()