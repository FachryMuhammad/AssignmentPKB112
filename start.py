from mnist import MNIST
mndata = MNIST('./data')
images,labels = mndata.load_training()
t_images, t_pabels = mndata.load_testing()