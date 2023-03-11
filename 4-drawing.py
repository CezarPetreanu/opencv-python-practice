import cv2
import numpy

cap = cv2.VideoCapture(0)
frame = cap.read()

print("Shape test")
img = numpy.zeros((int(cap.get(4)), int(cap.get(3)), 3), numpy.uint8)
img = cv2.rectangle(img, (20, 20), (50, 60), (255, 0, 0), -1)
img = cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
img = cv2.circle(img, (img.shape[1]//2, img.shape[0]//2), 64, (0, 0, 255), 5)

cv2.imshow("Draw", img)

cv2.waitKey(0)


print("Moving shape test")
img = numpy.zeros((int(cap.get(4)), int(cap.get(3)), 3), numpy.uint8)
x = 5
y = img.shape[0]//2
move = 1
while True:
    img = cv2.circle(img, (x, y), 70, (0, 0, 0), -1)
    img = cv2.circle(img, (x, y), 64, (255, x*255/640, 255), -1)
    x += move

    if (x == 0 or x == 640):
        move *= -1

    cv2.imshow("Draw", img)

    if (cv2.waitKey(1) == ord('q')):
        break

print("Webcam test")
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame = cap.read()
    frame = cv2.rectangle(frame, (8, 8),
                          (frame.shape[1]-8, frame.shape[0]-8), (0, 255, 0), 2)
    frame = cv2.putText(frame, "Webcam", (20, 40), font,
                        1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("Draw", frame)
    if (cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
