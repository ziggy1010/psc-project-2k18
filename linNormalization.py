import cv2 as cv; import numpy as np; from glob import glob

# img = cv.imread('test_images/majin_kanon/IMG_5141.JPG', cv.IMREAD_GRAYSCALE)
def linNormalization(img, name):
    img_arr = np.array(img)
    dst = np.zeros((4000, 3000))
    img_mod = cv.normalize(img_arr, dst, 0, 255, norm_type = cv.NORM_MINMAX , dtype= cv.CV_32F)
    cv.imwrite('greyscaled-pics/third_method' + name, img_mod)

for fn in glob("test_images/majin_kanon/*"):
    print(fn)
    img = cv.imread(fn, 0)
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    linNormalization(img, fn.split("/")[-1])