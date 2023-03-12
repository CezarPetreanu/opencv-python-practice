import cv2
import numpy

cap = cv2.VideoCapture(0)
mode = 0

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    if (mode == 0):
        cv2.imshow("Webcam", frame)
    elif (mode == 1):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow("Webcam", hsv)
    else:
        low_red = numpy.array([0, 148, 173])
        up_red = numpy.array([35, 255, 255])
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, low_red, up_red)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("Webcam", result)

    k = cv2.waitKey(1)

    if (k == ord('w')):
        mode += 1
        if (mode > 2):
            mode = 0
    elif (k == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
