import numpy as np
import cv2

path = "H:\\imageprocessingsection\\sec61\\img1.jpeg"
image = cv2.imread(path)
cv2.imshow("ori",image)

# transition

# m = np.float32([[1,0,x],[0,1,y]])
m = np.float32([[1,0,50],[0,1,20]])
shifted = cv2.warpAffine(image , m ,(image.shape[1], image.shape[0]))
cv2.imshow("shifted",shifted)

# transition function
def transition(image,x,y):
    m = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, m, (image.shape[1], image.shape[0]))
    return shifted

img_trans = transition(image,50,90)
cv2.imshow("img_trans",img_trans)


# rotaion
center = (image.shape[1]//2, image.shape[0]//2)
s = cv2.getRotationMatrix2D(center,45,1.0)
rotated = cv2.warpAffine(image , s ,(image.shape[1], image.shape[0]))
cv2.imshow("rotated",rotated)

#resizing
def resize (img , width=None,height=None,inter=cv2.INTER_AREA):
    dim = None
    (h,w) = img.shape[:2]
    if (width is None):
        r = height /float(h)
        dim = (int(w*r) ,height)

    elif (height is None):
        r = width / float(w)
        dim = (width,int(h * r))

    else:
        return img
    resized = cv2.resize(img,dim,interpolation=inter)
    return resized

resized = resize(image,width=1000)
cv2.imshow("resized",resized)

cv2.waitKey(0)