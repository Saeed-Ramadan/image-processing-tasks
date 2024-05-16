import numpy as np
import cv2

path = "H:\\imageprocessingsection\\sec62\\img1.jpeg"
image = cv2.imread(path)
cv2.imshow("ori", image)

# flipping
flipped = cv2.flip(image, 1)
cv2.imshow("flipped horiY", flipped)

flipped = cv2.flip(image, 0)
# cv2.imshow("flipped vertically",flipped)

flipped = cv2.flip(image, -1)
# cv2.imshow("flipped horiY & vertically",flipped)


# arithmetic

layer = np.ones(image.shape, dtype="uint8") * 50
# تفتيح
arithmetic_add = cv2.add(image, layer)
cv2.imshow("arithmetic_add", arithmetic_add)
# تغميق
arithmetic_subtract = cv2.subtract(image, layer)
cv2.imshow("arithmetic_subtract", arithmetic_subtract)

# gates
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

canvas = np.zeros((300, 300, 3), dtype="uint8")
cv2.rectangle(canvas, (25, 25), (275, 275), red, -1)
cv2.imshow("rectangle",canvas)

canvas2 = np.zeros((300, 300, 3), dtype="uint8")
cv2.circle(canvas2, (canvas2.shape[1] // 2, canvas2.shape[0] // 2), 150, red, -1)
cv2.imshow("circle",canvas2)

bitwise_add = cv2.bitwise_and(canvas, canvas2)
cv2.imshow("bitwise_add",bitwise_add)

bitwise_or = cv2.bitwise_or(canvas, canvas2)
cv2.imshow("bitwise_or",bitwise_or)

bitwise_not = cv2.bitwise_not(canvas2)
cv2.imshow("bitwise_not",bitwise_not)

bitwise_xor = cv2.bitwise_xor(canvas, canvas2)
cv2.imshow("bitwise_xor",bitwise_xor)

# لو عايز احط الصوره فى مربع
img = np.zeros(image.shape, dtype="uint8")
(cx, cy) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.rectangle(img, (cx - 75, cy - 75), (cx + 75, cy + 75), (255, 255, 255), -1)
cv2.imshow("rectangle_img",img)
masked = cv2.bitwise_and(image, img)
cv2.imshow("masked",masked)

# split and merge channel
(B, G, R) = cv2.split(image)
cv2.imshow("R",R)
cv2.imshow("G",G)
cv2.imshow("B",B)

split_img = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("R",cv2.merge([split_img,split_img,R]))
cv2.imshow("G",cv2.merge([split_img,G,split_img]))
cv2.imshow("B",cv2.merge([B,split_img,split_img]))

# color space

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)

hab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("hab", hab)
cv2.waitKey(0)
