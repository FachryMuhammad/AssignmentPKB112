import numpy as np

def print_statistics(images, t_images, labels, t_labels):
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

#def add_thetas(theta):
#    return

def hypothesis(images, labels):
    (x,y) = images.shape
    num_classes= len(labels)
    trans= np.matrix.transpose(x)

    add_thetas =0
    for i in range (num_classes-1):
        theta = np.random.rand(x,(y-1))*0.001
        add_thetas += theta * trans

    b=labels
    a=np.exp(theta)
    h = 1/a*b
    return h