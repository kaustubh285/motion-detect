import cv2, time

video=cv2.VideoCapture(0)

check , frame=video.read()

time.sleep(3)
for frames in frame:
    cv2.imshow("Capturing",frame)

cv2.waitKey(0)
video.release()
cv2.destroyAllWindows
