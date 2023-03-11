import cv2

img = cv2.imread('assets/pisica.jpg', 1)
print("IMAGE (BGR): ")
print(img)
print("SIZE (H, W, CH): ")
print(img.shape)

# original image
cv2.imshow('Imagine (Original)', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# invert colors
print("loading... Inverted colors")
img_modified = cv2.bitwise_not(img)

cv2.imshow('Imagine (Culori inversate)', img_modified)
cv2.waitKey(0)
cv2.destroyAllWindows()

# blue tint
img_modified = img
print("loading... Blue Tint")
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		new_blue = img[i][j][0]
		if new_blue+25 <= 255:
			new_blue += 25
		img_modified[i][j] = [new_blue, img[i][j][1], img[i][j][2]]

cv2.imshow('Imagine (Culoare albastra)', img_modified)
cv2.waitKey(0)
cv2.destroyAllWindows()

# copy face
img_modified = img
print("loading... Copy Face")
clip = img[477:719, 310:580]
img_modified[20:262, 20:290] = clip

cv2.imshow('Imagine (Fata copiata)', img_modified)
cv2.waitKey(0)
cv2.destroyAllWindows()