import numpy as np
import cv2


img = cv2.imread('card.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
x, y, w, h = 0, 0, 0, 0

# define the bounds for the colours we want to find in the contour
lower_bound = np.array([220])
upper_bound = np.array([255])

mask = cv2.inRange(imgray, lower_bound, upper_bound)
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

if len(contours) != 0:
    # draw the contours that were found in blue (for testing)
    # cv2.drawContours(img, contours, -1, 255, 2)

    # find the biggest area contour
    c = max(contours, key=cv2.contourArea)

    x, y, w, h = cv2.boundingRect(c)
    # draw a rectangle around the biggest contour
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv2.imshow("orig", img)
cv2.imshow("mask", imgray)

# crop the image with the coordinates of the maximum area contour we found
crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)

cv2.waitKey(0)
