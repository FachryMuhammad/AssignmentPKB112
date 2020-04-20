from mnist import MNIST
import numpy as np
from lib import *

mndata = MNIST('./data')
images,labels = mndata.load_training()
t_images, t_labels = mndata.load_testing()

images = np.array(images)
t_images = np.array(t_images)
labels = np.array(labels)
t_labels = np.array(t_labels)

print("training instances ;", images.shape[0])
print("testing instances ;", t_images.shape[0])

num_class = len(np.unique(labels))

print("there are :", num_class, "classes")

for i in range(num_class):
    print("class", i, "instances : ", np.sum(labels==i))

print("statistics for testing")

for i in range(num_class):
    print("class :", i, "instances : ", np.sum(t_labels==i))


print_statistics(images, t_images, labels, t_labels)

#convert .m file ex1c_softmax.m

#train.X = [ones(1,size(train.X,2)); train.X];     line 16 
#test.X = [ones(1,size(test.X,2)); test.X];             17
#train.y = train.y+1; % make labels 1-based.            18
#test.y = test.y+1; % make labels 1-based.              19
#theta = rand(n,num_classes-1)*0.001;                   32

(x,y) = images.shape
bias = np.ones((x,1))
images = np.hstack((bias,images))

(x2,y2) = t_images.shape
t_bias = np.ones((x2,1))
t_images = np.hstack((t_bias,t_images))

#n=np.size(images)
num_class = len(np.unique(labels))
#num_class = len(labels)


#test
theta=np.random.rand(x,y-1)*0.001
#print (theta)
