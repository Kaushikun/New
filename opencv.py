import cv2 as cv

# Use the absolute path to the image
image_path = '/home/kaushikun/Documents/photo/images.jpg'

# Load and display the image
img = cv.imread(image_path)
cv.imshow('Image Window', img)
cv.waitKey(0)
cv.destroyAllWindows()
