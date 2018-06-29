import pylab as plt; import cv2 as cv
import milk.supervised.tree; import numpy as np
import milk.supervised.adaboost
from milksets import wine
import milk.supervised.multi
from clahe import clahe
from glob import glob
from histEqualisation import *

#TODO: klasifikatori, slike

for fn in glob("test_images/majin_kanon/*"):
    print(fn)
    img = cv.imread(fn, 0)
    img = img.flatten()
    img2 = histogram_equalisation(img, fn.split("/")[-1])
   
    features = np.array(img)
    labels = np.array(img)

    weak = milk.supervised.tree.stump_learner()
    learner = milk.supervised.adaboost.boost_learner(weak)
    learner = milk.supervised.multi.one_against_one(learner)

    model = learner.train(features, labels)
    new_label = model.apply()

    confusion_matrix = int(milk.nfoldcrossvalidation(features, labels))
    acc = confusion_matrix.trace()/float(confusion_matrix.sum)
    print('uspesnost je ' + acc)
    #print(new_label)
    # colors = "rgb"
    # codes = "xo"
    # for y,x,r,p in zip(features.T[0], features.T[1], labels, predictions):
    #     code = codes[int(r == p)]
    #     plt.plot([y],[x], colors[p]+code)

#plt.show()