import milk.supervised.tree; import milk.supervised.adaboost 
from milksets import wine; import milk.supervised.multi 
from histEqualisation import histogram_equalisation
from glob import glob; import cv2 as cv; import numpy as np

for fn in glob("test_images/majin_kanon/*"):
    print(fn)
    img = cv.imread(fn, 0)
    hist =  np.array(img.flatten())

    img2 = histogram_equalisation(img, fn.split("/")[-1])
    hist_output = np.array(img2.flatten())

    weak = milk.supervised.tree.stump_learner()
    learner = milk.supervised.adaboost.boost_learner(weak)
    learner = milk.supervised.multi.one_against_one(learner)

    features = np.array(hist)
    labels = np.array(hist_output)

    print(features)
    print(labels)

    model = learner.train(features, labels)
    
    # print(model.apply())