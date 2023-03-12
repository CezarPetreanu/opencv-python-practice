import cv2
import numpy

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades+"haarcascade_eye.xml")

googly_eye = cv2.imread("assets/googly_eye.png", 1)
showEyes = False

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 6)
    print(faces)
    for (x, y, w, h) in faces:
        if (not showEyes):
            cv2.rectangle(frame, (x, y), (x+w, y+h), [0, 255, 0], 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.15, 6)
        for (ex, ey, ew, eh) in eyes:
            px = (ex+ex+ew)//2
            py = (ey+ey+eh)//2
            if (not showEyes):
                cv2.rectangle(roi_color, (ex, ey),
                              (ex+ew, ey+eh), [255, 0, 0], 2)
                cv2.circle(roi_color, (px, py), 2, [0, 0, 255])
            else:
                cv2.circle(roi_color, (px, py), ew//2, [255, 255, 255], -1)
                cv2.circle(roi_color, (px, py+8), ew//4, [0, 0, 0], -1)

    cv2.imshow("Face detection", frame)

    k = cv2.waitKey(1)
    if (k == ord('w')):
        showEyes = not showEyes
    if (k == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
