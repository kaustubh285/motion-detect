import cv2, time
from datetime import datetime
import pandas as pd

status = [None, None]
time = []
df = pd.DataFrame(columns=["Start", "End"])
vid = cv2.VideoCapture(0)
first_frame = None
while True:
    check, frame = vid.read()

    motion_status = 0

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0) # (img, (blurriness value of height and width), standard deviation)
    #Gaussianblur removes noise and improves accuracy

    if first_frame is None:
        first_frame = gray
        continue

    delta = cv2.absdiff(first_frame,gray)
    thresh = cv2.threshold(delta, 30, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations= 2)
    #dilate(frame to dilate, kernel array, number of times to iterate)

    (_,cnts,_)=cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

    for conts in cnts:
        if cv2.contourArea(conts)  < 10000:
            continue
        motion_status = 1
        (x,y,w,h) = cv2.boundingRect(conts)
        cv2.rectangle(frame, (x,y) , (x+w , y+h), (0,255,0) , 3)
    status.append(motion_status)

    status = status[-2:]


    if status[-1]==1 and status[-2]==0:
        time.append(datetime.now())
    if status[-1]==0 and status[-2]==1:
        time.append(datetime.now())
    cv2.imshow("Capturing",gray)
    cv2.imshow("diff",delta)
    cv2.imshow("thresh", thresh)
    cv2.imshow("color frame",frame)
    key = cv2.waitKey(1)

    if key==ord('q'):
        if motion_status==1:
            time.append(datetime.now())
        break
print(status)
print(time)

df["Start"]= time[0::2]
df["End"]= time[1::2]

df.to_csv("enter-exit")
vid.release()
cv2.destroyAllWindows
