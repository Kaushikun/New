import cv2 as cv

image_path = '/home/kaushikun/Documents/photo/images.jpg'

img = cv.imread(image_path)
cv.imshow('Image Window', img)
cv.waitKey(0)
cv.destroyAllWindows()
