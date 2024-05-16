import numpy as np
import cv2

photo = "H:\\imageprocessingsection\\sec3\\img1.jpeg"
image = cv2.imread(photo)
print("width = {}", format(image.shape[1]))
print("height = {}", format(image.shape[0]))
# channel 3 mean the image contain from 3 colors (RGB)
print("channel = {}", format(image.shape[2]))

# get the color of pixel
(b,g,r) = image[100,100]
print("red= {}", format(r))
print("green= {}", format(g))
print("blue= {}", format(b))
cv2.imshow("ori", image)

cv2.waitKey(0)
