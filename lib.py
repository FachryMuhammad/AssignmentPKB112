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

def add_thetas(images, theta):
    sum = theta[0]
    for i in range(1,len(images.iloc[0])):
        sum += np.sum(theta[i+1]*images.iloc[:,i])
    sum_exp_thetas= np.exp(sum)    
    return sum_exp_thetas

def hypothesis(theta, images, labels):
    #(x,y) = images.shape
    im_size = np.unique(labels)
    t=theta
    vec_theta=[]
    sum_theta=[]

    for i in range (im_size):
        vec_theta.append(add_thetas(images, t[:,i]))
        sum_theta = np.sum(vec_theta)

    a=vec_theta
    b=sum_theta
    h = a/b
    return h