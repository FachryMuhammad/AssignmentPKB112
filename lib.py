import numpy as np

print_statistics(images, t_images, labels, t_labels):
    #number of training dataset
    len(labels)
    #number of test dataset
    len(t_labels)
    #number of class
    len(np.unique(labels))
    #number of instances per class on training
    for i in np.unique(labels):
        np.sum(labels==i)
    #number of instances per class on test dataset
    for i in np.unique(t_labels):
        np.sum(t_labels==i)

#From  .m file ex1c_softmax.m

#train.X = [ones(1,size(train.X,2)); train.X]; 
#test.X = [ones(1,size(test.X,2)); test.X];


(x,y) = images.shape
bias = np.ones((m,1))
images = np.hstack((bias,images))
(x2,y2) = t_images.shape
t_bias = np.ones((m2,1))
t_images = np.hstack((t_bias,t_images))