import cv2
cv2.destroyAllWindows()
img = cv2.imread('/home/kaushikun/Desktop/Opencv Tutorial/Images and videos/Dog.jpg',0)
img=cv2.resize(img,(1000,1000))
img=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) 
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()