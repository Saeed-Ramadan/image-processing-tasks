import numpy as np
import cv2

photo = "H:\\imageprocessingsection\\sec3\\img1.jpeg"
image = cv2.imread(photo)
print("width = {}", format(image.shape[1]))
print("height = {}", format(image.shape[0]))
# channel 3 mean the image contain from 3 colors (RGB)
print("channel = {}", format(image.shape[2]))

# get the color of pixel
(b, g, r) = image[100, 100]
print("red= {}", format(r))
print("green= {}", format(g))
print("blue= {}", format(b))

# تغير لون pixel
image[25, 0] = (0, 0, 255)
(b, g, r) = image[25, 0]
print("pixel at (25,0) red : {} , green : {} , blue : {}".format(r, g, b))
cv2.imshow("ori", image)

# croped the image
croped = image[0:100, 0:155]
cv2.imshow("croped", croped)

# لون جزء من الصوره بلون
copy = image.copy()
copy[0:25, 0:25] = (0, 255, 0)
cv2.imshow("copy", copy)

cv2.waitKey(0)
