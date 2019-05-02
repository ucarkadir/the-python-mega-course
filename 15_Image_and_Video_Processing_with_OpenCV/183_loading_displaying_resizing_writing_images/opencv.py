import cv2

img=cv2.imread("galaxy.jpg", 0)

print(type(img))
print(img) # give us x and y
print(img.shape) # resulation
print(img.ndim)
'''
# dimensions : 
    img=cv2.imread("galaxy.jpg", 0) = 2
    img=cv2.imread("galaxy.jpg", 1) = 3
'''


# resized_image=cv2.resize(img, (1000,500))
resized_image=cv2.resize(img, ( int(img.shape[1]/2),  int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)

# cv2.waitKey(2000) # 2000 ms
cv2.waitKey(0) # 
cv2.destroyAllWindows()