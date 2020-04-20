
from mnist import MNIST
import numpy as np
from lib import *

mndata = MNIST('./data')
images,labels = mndata.load_training()
t_images, t_labels = mndata.load_testing()


#convert .m file ex1c_softmax.m

#train.X = [ones(1,size(train.X,2)); train.X];     line 16 
#test.X = [ones(1,size(test.X,2)); test.X];             17
#train.y = train.y+1; % make labels 1-based.            18
#test.y = test.y+1; % make labels 1-based.              19

(x,y) = images.shape
bias = np.ones((x,1))
images = np.hstack((bias,images))


(x2,y2) = t_images.shape
t_bias = np.ones((x2,1))
t_images = np.hstack((t_bias,t_images))
