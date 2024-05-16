import numpy as np
import cv2

# علشان احدد الاطار الخارجى اللى هرسم جواه
canvas = np.zeros((300, 300, 3), dtype="uint8")
cv2.imshow("ori", canvas)
# لو عايز ارسم خط
cv2.line(canvas, (25, 25), (275, 275), (0, 255, 0), 6)
cv2.imshow("line", canvas)

# لو عايز ارسم مستطيل
cv2.rectangle(canvas, (25, 25), (50, 50), (0, 0, 250), 6)  # 6دى يعنى سمك الخط لو عملتها -1 هتعمله fill
cv2.imshow("rectangle", canvas)

# لو عايز ارسم دائره
canvas2 = np.zeros((300, 300, 3), dtype="uint8")
center = (canvas2.shape[1] // 2, canvas2.shape[0] // 2)
cv2.circle(canvas2, center, 100, (255, 0, 0), 6)  # 6دى يعنى سمك الخط لو عملتها -1 هتعمله fill
cv2.imshow("circle", canvas2)

# لو عايز ارسم دوائر كتير
canvas3 = np.zeros((300, 300, 3), dtype="uint8")
center = (canvas3.shape[1] // 2, canvas3.shape[0] // 2)
for r in range(0, 255, 10):
    cv2.circle(canvas3, center, r, (255, 0, 0), )
cv2.imshow("circles", canvas3)

# لو عايز ارسم دوائر عشوائية
canvas4 = np.zeros((300, 300, 3), dtype="uint8")
center = (canvas3.shape[1] // 2, canvas3.shape[0] // 2)
for i in range(0, 50):
    r = np.random.randint(10, 100)
    color = np.random.randint(0, 256, (3,)).tolist()
    center = np.random.randint(0, 300, (2,))
    cv2.circle(canvas4, center, r, color, -1)

cv2.imshow("circles2", canvas4)

# لو عايز ارسم مستطيلات عشوائية
canvas5 = np.zeros((300, 300, 3), dtype="uint8")

for i in range(0, 50):
    color = np.random.randint(0, 256, (3,)).tolist()
    # Randomize the top-left and bottom-right coordinates of the rectangle
    pt1 = np.random.randint(0, 300, (2,))
    pt2 = np.random.randint(0, 300, (2,))
    # Ensure that pt2 is to the bottom-right of pt1
    pt1, pt2 = np.minimum(pt1, pt2), np.maximum(pt1, pt2)
    # Draw the rectangle
    cv2.rectangle(canvas5, tuple(pt1), tuple(pt2), color, -1)

cv2.imshow("rectangles", canvas5)
cv2.waitKey(0)
cv2.waitKey(0)
