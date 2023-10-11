
import numpy as np
import cv2
# load image in color
img = cv2.imread("photo kb.png")
#load image in grey format
gimg = cv2.imread("photo kb.png",0)


(h, w) = img.shape[:2]
cgimg=255-gimg
# calculate the center of the image
center = (w / 2, h / 2)

angle30 = -30
angle45 = -45
angle90 = -90

scale = 1.0

# Perform the Anti-clockwise rotation holding at the centre
# 30 degrees
M = cv2.getRotationMatrix2D(center, angle30, scale)
rotated30 = cv2.warpAffine(img, M, (h, w))

# 45 degrees
M = cv2.getRotationMatrix2D(center, angle45, scale)
rotated45 = cv2.warpAffine(img, M, (h,w))

# 90 degrees
M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M, (h, w))

#scaling operation
sca = cv2.resize(img, (0, 0), fx=0.5, fy=1)

cv2.imshow('photo image', img)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

cv2.imshow('photo complement image', cgimg)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

cv2.imshow('photo grey image', gimg)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

cv2.imshow('photo rotated by 30 degrees', rotated30)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

cv2.imshow('photo rotated by 45 degrees', rotated45)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

cv2.imshow('photo rotated by 90 degrees', rotated90)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

cv2.imshow('photo scaling operation',sca)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image


