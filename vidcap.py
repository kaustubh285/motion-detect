import cv2, time

vid = cv2.VideoCapture(0)
no_of_frames_taken=1
while True:
    no_of_frames_taken=no_of_frames_taken+1
    check, frame = vid.read()
    #time.sleep(1)
    cv2.imshow("Capturing",frame)
    key = cv2.waitKey(1)

    if key==ord('q'):
        break
print(no_of_frames_taken)
vid.release()
cv2.destroyAllWindows
