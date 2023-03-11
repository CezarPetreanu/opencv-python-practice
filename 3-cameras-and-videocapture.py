import numpy as np
import cv2

cap = cv2.VideoCapture(0)

print("Single frame")

while True:
    ret, frame = cap.read()
    # ret   - return, checks if capture worked
    # frame - camera image

    cv2.imshow("Webcam", frame)

    if (cv2.waitKey(1) == ord('q')):
        break

print("Four frames, different flips")
while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))
    # other properties:
    # https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d

    image = np.zeros(frame.shape, np.uint8)
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[0:height//2, 0:width//2] = small_frame
    image[0:height//2, width//2:width] = cv2.flip(small_frame, -1)
    image[height//2:height, 0:width//2] = cv2.flip(small_frame, 0)
    image[height//2:height, width//2:width] = cv2.flip(small_frame, 1)

    cv2.imshow("Webcam", image)

    if (cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
