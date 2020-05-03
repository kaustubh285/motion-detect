import cv2

img=cv2.imread("galaxy.jpg",0)

print(img.shape)

img2=cv2.resize(img,(int(img.shape[0]/2),int(img.shape[1]/2)))
print(img2.shape)
cv2.imshow("galaxy",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("New.jpg",img2)
