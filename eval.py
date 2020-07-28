import cv2

cams_test = 10
for id in range(0, cams_test):
    cap = cv2.VideoCapture(id)
    test, frame = cap.read()
    if test:
        print("id : "+str(id)+" /// result: "+str(test))
    cap.release()