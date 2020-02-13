import cv2, time, pandas
from datetime import datetime

FIRST_FRAME = None
STATUS_LIST = [None, None]
TIMES = []
DF = pandas.DataFrame(columns=["Start", "End"])

video=cv2.VideoCapture(0)

print(0)

while True:
    check, frame = video.read()
    status=0
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if FIRST_FRAME is None:
        FIRST_FRAME = gray
        continue

    delta_frame=cv2.absdiff(FIRST_FRAME,gray)

    thresh_frame=cv2.threshold(delta_frame,30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    (_,cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1

        (x,y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)
    STATUS_LIST.append(status)
    
    STATUS_LIST = STATUS_LIST[-2:]        

    if STATUS_LIST[-1] == 1 and STATUS_LIST[-2] == 0:
        TIMES.append(datetime.now())
    if STATUS_LIST[-1] == 0 and STATUS_LIST[-2] == 1:
        TIMES.append(datetime.now())

    cv2.imshow("Capturing", gray)
    cv2.imshow("Delta Frema", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)
    
    key=cv2.waitKey(1) # 1 ms
    
    if key==ord('q'):
        if status==1:
            TIMES.append(datetime.now())
        break
    
#print(STATUS_LIST)
print(TIMES)

for i in range(0, len(TIMES), 2):
    DF = DF.append({"Start":TIMES[i], "End":TIMES[i+1]}, ignore_index=True)

DF.to_csv("TIMES.csv")

video.release()
cv2.destroyAllWindows