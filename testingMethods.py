import cv2 as cv

img = cv.imread('test_images/majin_kanon/IMG_5141.JPG', 0)
#cv.imshow('kita', img)
# cv.imwrite('kita.jpg', img)
# cv.waitKey()
img_modified = cv.imread('greyscaled-pics/IMG_5141.JPG', 0)

for i in range(5):
    for j in range(2):
        print(img_modified[i][j])
print("######")

for i in range(5):
    for j in range(2):
        print(img[i][j])

#print(img_modified[0:2][0:2])
#print("#####################")
#print(img[0:2][0:2])