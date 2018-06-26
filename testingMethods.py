import cv2 as cv

img = cv.imread('test_images/majin_kanon/IMG_5141.JPG', 0)
img_modified = cv.imread('greyscaled-pics/IMG_5141.JPG')

#print(img.shape)
for i in range(img_modified.shape[0]):
    for j in range(img_modified.shape[1]):
        output = img_modified[i][j]
        print(output)