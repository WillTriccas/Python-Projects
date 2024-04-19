import cv2
import time
import pandas
from datetime import datetime

first_frame = None

video = cv2.VideoCapture(0)

df = pandas.DataFrame(columns=["Start", "End"])

status_list = [None,None] #Need to put two none values here because later we search for the 2nd last and last item in the list and it cannot do that with an empty list
times_list = []

while True:
    check, frames = video.read()
    status = 0
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)  

    threshold_frame = cv2.threshold(delta_frame,30, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations= 10)

    (cnts,_) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) <5000:
            continue
        status = 1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frames, (x,y), (x+w,y+h), (0,255,0), 3)

        #having nothing after the continue is basically like saying, if there is a contour area lower than 1000, go back and search for another one,
        #but if there is, ignore the continue and carry on the the x,y,w,h line.

    status_list.append(status)

    status_list = status_list[-2:]   #This is to tackle the memory problem of the camera being left on for a long while, we only need 2 status items to log when something entered/exited the frame

    if status_list[-1] == 1 and status_list[-2] ==0:
        times_list.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] ==1:
        times_list.append(datetime.now())

    #This conditional here will mark the time when something enters or exits the camera frame and is big enough to be picked up by our contour for loop above


    cv2.imshow("Capturing", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Delta", threshold_frame)
    cv2.imshow("Coloured Frame with rectangle around new objects", frames)
    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times_list.append(datetime.now())
        break

for i in range(0,len(times_list),2):
    df = df.append({"Start": times_list[i], "End" : times_list[i+1]}, ignore_index= True)
    #Have put ignore index there otherwise the script wont work as list isnt populated initially.

df.to_csv("ObjectTimeStamps.csv")

print(times_list)
print(status_list)
video.release()
cv2.destroyAllWindows()