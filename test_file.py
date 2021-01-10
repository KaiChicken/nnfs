import numpy as np
#from test1 import class2
#import test1.class2
import test2
import cv2
#import activation_function as af
#b = af.test_class.a
#print (b)
ob = test2.class2()


image_data = cv2.imread("images.jpg", cv2.IMREAD_GRAYSCALE)
image_data = 255 - image_data
#image_data.reshape(1,-1)
print(image_data.shape)
print(type(image_data))
print(type(image_data[0][0]))
print(range(len(image_data)))

a = np.arange(20)
np.random.shuffle(a)
a = np.clip(a,4,6)
print(a.shape)
print(a)

a = np.exp(1)
print(a)

a = np.arange(0,24).reshape([2,3,4])
print(a)
print(a.shape)
print(np.exp(1))

a = np.random.randn(4,5)
print(a)