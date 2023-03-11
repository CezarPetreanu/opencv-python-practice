import cv2

img = cv2.imread('assets/pisica.jpg', 1)
# -1 = imagine color, fara transparenta
#  0 = imagine alb-negru
#  1 = imagine color, transparenta
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
#img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_pisica.jpg', img)
cv2.imshow('Imagine', img)
cv2.waitKey(0)
cv2.destroyAllWindows()