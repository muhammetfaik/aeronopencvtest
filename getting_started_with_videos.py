import cv2

cap = cv2.VideoCapture(0)
print(cap.isOpened())

while(True):
    ret,frame = cap.read()

    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BG2GRAY)
    cv2.imshow('frame',gray)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
