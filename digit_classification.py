# -*- coding: utf-8 -*-
"""Digit Classification

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16dAY2J2Ssu4ga1xNj0gbsjttEewJuHDx

Importing the Dependencies.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from google.colab.patches import cv2_imshow
from PIL import Image
import tensorflow as tf
tf.random.set_seed(3)
from tensorflow import keras
from keras.datasets import mnist
from tensorflow.math import confusion_matrix

"""Loading the MNIST data from the keras.datsets"""

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

print(X_train.shape, Y_train.shape, X_test.shape, Y_test.shape)

"""X_train:
  images: 60000,
  image dimension: 28*28,
  grayscale
"""

# dispaly a image
plt.imshow(X_train[4507])
plt.show()

# corresponding label
print(Y_train[4507])

# scaling the values.

X_train  = X_train/255
X_test = X_test/255

"""Building the Neural Network"""

# setting up the layers of the neural network

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(50, activation = 'relu'),
    keras.layers.Dense(50, activation = 'relu'),
    keras.layers.Dense(10, activation = 'sigmoid')
])

# compiling the Neural Network

model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])

#training the neural network

model.fit(X_train, Y_train, epochs=10)

"""Training data accuracy = 98.86%"""

loss, accuracy = model.evaluate(X_test, Y_test)

print(accuracy)

"""Test data accuracy = 97.31%"""

plt.imshow(X_test[0])
plt.show()

print(Y_test[0])

Y_pred = model.predict(X_test)

print(Y_pred[0])

"""model.predict() gives the prediction probability of each class for that data point"""

label_for_first_imamge = np.argmax(Y_pred[0])
print(label_for_first_imamge)

Y_pred_label = [np.argmax(i) for i in Y_pred]
print(Y_pred_label)

"""Confusion Matrix"""

conf_mat = confusion_matrix(Y_test, Y_pred_label)
print(conf_mat)

plt.figure(figsize=(15,7))
sns.heatmap(conf_mat, annot = True, fmt='d', cmap = 'Blues')
plt.ylabel('True Labels')
plt.xlabel('Predicted Labels')

"""Predictive System"""

# input_image_path = input('Path of the image to be predicted: ')

# input_image = cv2.imread(input_image_path)

# cv2_imshow(input_image)

# grayscale = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)

# input_image_resize = cv2.resize(grayscale, (28, 28))

# input_image_resize = input_image_resize/255

# image_reshaped = np.reshape(input_image_resize, [1,28,28])

# input_prediction = model.predict(image_reshaped)

# input_pred_label = np.argmax(input_prediction)

# print('The Handwritten Digit is recognised as ', input_pred_label)