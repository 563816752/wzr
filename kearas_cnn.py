import numpy as np
import pandas as pd 
from keras.utils import np_utils
from keras.datasets import mnist
import matplotlib.pyplot as plt
def plot_image(image):
    fig=plt.gcf()
    fig.set_size_inches(2,2)
    plt.imshow(image,cmap='binary')
    plt.show()
(X_trian_image,y_trian_label),\
(X_test_image,y_test_label)=mnist.load_data()
# 这个反斜杠没搞清楚
x_Train=x_train_image.reshape(60000,784).astype('float32')
x_Test=x_test_image.reshape(10000,784).astype('float32')
x_Train_normalize=x_Train/255
x_Test_normalize=x_Test/255
y_Train_onehot=np_utils.to_c
