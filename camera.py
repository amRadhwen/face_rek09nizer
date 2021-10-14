# import opencv
import cv2

# define vi capture object

video = cv2.VideoCapture(0)

# capture loop
counter = 0
while True:
    # capture video frame by frame
    ret, frame = video.read()

    # display the resulting frame
    cv2.imshow("frame", frame)

    # define capture quit button (in this case it's the 'q' button)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

    # define photo capture key (in this case
    if cv2.waitKey(1) & 0XFF == ord('c'):
        cv2.imwrite('rek09nizer'+str(counter)+".png", frame)

    counter += 1

# release the capture object after exit the loop
video.release()

# destroy the window
cv2.destroyAllWindows()