import cv2 as cv; import numpy as np; from glob import glob; from matplotlib import pyplot as plt

dir_in = input()
dir_out = input()

def linNormalization(img, name):
    img_arr = np.array(img)
    dst = np.zeros((4000, 3000))
    img_mod = cv.normalize(img_arr, dst, 0, 255, norm_type = cv.NORM_MINMAX , dtype= cv.CV_32F)
    cv.imwrite("greyscaled-pics/third_method/" + dir_out + "/"+ name, img_mod)
    # linHistogram(img)
    # linHistogram(img_mod)

def linHistogram(img):
    plt.hist(img.flatten(), 256, [0, 256], color = 'r')
    plt.xlim([0, 256])
    plt.legend(('histogram')) 
    plt.show()

for fn in glob("test_images/"+ dir_in +"/*"):
    print(fn)
    img = cv.imread(fn, 0)
    linNormalization(img, fn.split("/")[-1])