'''
activation
    relu
    softmax
    sigmoid
    linear

optimizer
    gradient descent
    gradient ascent
    adam
    adagrad
    rms prop

loss
    categorical cross entropy
    binery cross entropy
    mean square error

accuracy
    categorical
    regression
forward
    fully connected layers
    random connected layers
    ramdon connected neurons

backward

dropout

placeholder object
    file paths
        input file
        output file
            parameters + result + data size + time +
    input data
    output data
    parameters
        weights
        bias
    step input
    step output
    log

'''



def activation_relu(input):
    output = np.maximum(0,input)
    return output
    pass
def activation_relu_derivative(input):

    pass

def activation_softmax(input):

    pass
def activation_sigmoid(input):
    output = 1 / (1 + np.exp(input))
    return output

    pass
def activation_linear(input):
    pass
def optimizer_gradient_descent(input):
    pass


import numpy as np


a = np.eye(3,k=0)
b = np.arange(9).reshape(3,3)
c = np.dot(a,b)
print(c)

a = np.arange(10).clip(0,4).reshape(-1)
print(len(a.shape))
print(a)

b = np.random.randint(0,5,20)
c = np.eye(5)[b]

print(c)
#print(d.shape)
'''
import numpy as np

#generate a matrix
a = np.arange(0,12,1).reshape(3,-1)
print("\na \n",a)
print(a.shape)
b = np.random.rand(20).reshape(4,5)
b = np.random.rand(4,5)
print("\nb \n",b)
print(b.shape)
c = np.random.randint(0,20, size=(4,5))
c = np.random.randint(0,20, size=(20))
c = np.random.randint(10,20,20).reshape(4,5)

#create identity matrix
a = np.eye(5)
print("\na \n",a)
b = np.random.randint(0,5,20)
c = np.eye(5)[b]


#transpose
a = a.T
a = np.transpose(a)
print(a)
print(a.shape)

#dot function
a = np.arange(9).reshape(3,3)
b = a.dot(a)
b = np.dot(a,a)


'''


'''
#check numpy element data type
a = 1.
a = np.array(a).astype("float32")
print(a.dtype)
'''


'''
import time
time comparison between using maximum, max, if, to implement relu function
if 5 to 10 percent faster than maximum 
maximum 20% faster than max
max 

abc = np.array([])
start = time.time()
for a in range(100000):
    if a>0:
        abc = np.append(abc, a)
    else:
        abc = np.append(abc, a)
print(time.time()-start)

abc = np.array([])
start = time.time()
for a in range(100000):
    np.maximum(a,0)
    abc = np.append(abc, a)

print(time.time()-start)

abc = np.array([])
start = time.time()
for a in range(100000):
    np.max(a,0)
    abc = np.append(abc, a)
print(time.time()-start)
'''