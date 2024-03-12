# -*- coding: utf-8 -*-
"""Another copy of PERCEPTRON.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y5wm3mqcvUw5y-Q8H38HLwSy1p8hyrck

# Perceptron Learning Algorithm Code
"""

import numpy as np

W = np.zeros(2+1)
W

X=[2,3]
np.insert(X, 0, 1)

# initialization code
def __init__(self, input_size, lr=1, epochs=10, bias=1):
    self.W = np.zeros(input_size+bias)
    self.epochs = epochs
    self.lr = lr

# Activation function code which is a simple step function
def activation_fn(self, x):
        #return (x >= 0).astype(np.float32)
        return 1 if x >= 0 else 0

# Calculating dot product of W and X (input vector) and applying step function
def predict(self, x):
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        return a

# Perceptron Learning code running all the samples for given epochs or iterations
def fit(self, X, OutputLabel):
    no_of_smaples=4
    for _ in range(self.epochs):
        for i in range(no_of_samples):
            y = self.predict(X[i])
            e = OutputLabel[i] - y
            self.W = self.W + self.lr * e * np.insert(X[i], 0, 1)

"""# The complete executable code of Perceptron model"""

class Perceptron(object):
    """Implements a perceptron network"""
    def __init__(self, input_size, lr=1, epochs=100):
        self.W = np.zeros(input_size+1)
        # add one for bias
        self.epochs = epochs
        self.lr = lr
        self.loss_lst = []

    def activation_fn(self, x):
        #return (x >= 0).astype(np.float32)
        return 1 if x >= 0 else 0

    def predict(self, x):
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        return a

    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                x = np.insert(X[i], 0, 1)
                y = self.predict(x)
                e = d[i] - y
                self.W = self.W + self.lr * e * x
            self.loss_lst.append(e)

"""# AND GATE EXAMPLE WITH NO OF SAMPLES/RECORDS AS 4 AND EPOCHS AS 100"""

if __name__ == '__main__':
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    d = np.array([0, 1, 1, 0])

    perceptron = Perceptron(input_size=2)
    perceptron.fit(X, d)
    print(perceptron.W)

import matplotlib.pyplot as plt
x_axis = [int(x) for x in range(100)]
y_axis = perceptron.loss_lst
plt.plot(x_axis, y_axis)
plt.xlabel("iteration")
plt.ylabel("loss")
plt.show()

"""# Using the AND gate data, we should get a weight vector of [-3, 2, 1]. This means that the bias is -3 and the weights are 2 and 1 for x_1 and x_2, respectively.

# LETS TEST MANUALLY
# let us test for x=[0, 1]
"""

x=[1, 0, 1]
y= -3*1+2*0+1*1
y

"""# since it is a negative value on applying activation function we get zero which is correct"""