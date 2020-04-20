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

def SoftMaxMod(images, theta, theta_k, K):
    #(x,y) = images.shape
    exp_theta =add_thetas(images, theta_k)
    sum_exp = 0
    for i in range(K):
        sum_exp += add_thetas(images, theta[:,i])
    smm = exp_theta/sum_exp
    return smm

def CostFunct(images, labels, theta, K):
    m =  len(labels)
    #n = len(labels)
    sum_funct = 0
    for i in range(m):
        sum_K = 0
        for j in range(K):
            if labels.iloc[i,0] == j:
                sum_K += np.log(SoftMaxMod(images, theta, theta[:,j], K))
        sum_funct += sum_K
    cf=-sum_funct
    return cf

def GradDesc(images, labels, theta, k, K):
    #m =  len(labels)
    n = len(labels)
    sum_grad = []
    for i in range(n):
        if labels.iloc[i,0] == k:
            sum_grad.append(1 - SoftMaxMod(images, theta, theta[:,k], K))
        else:
            sum_grad.append(0 - SoftMaxMod(images, theta, theta[:,k], K))
    gd = -np.sum(sum_grad)
    return gd

def Thetan(images, y, theta, alpha, K):
    f = len(images.iloc[0])
    for i in range(K):
        for j in range(f):
            theta[j+1][i] = theta[j+1][i] - (alpha*GradDesc(images, y, theta, i, K))
            print("theta[{}][{}] = {}".format(j+1,i,theta[j+1][i]))
    return theta

def SoftLearn(images, y, theta, alpha, itr):
    cost = []
    for i in range(itr):
        theta = Thetan(images, y, theta, alpha, np.unique(y))
        cost.append(CostFunct(images, y, theta, np.unique(y)))
    return cost, theta