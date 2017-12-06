import pandas as pd
import numpy as np
from scipy import misc
import sys
import os
from sklearn.metrics import confusion_matrix

import keras
from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

from keras.utils import to_categorical

import sys
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import model_selection

import chainer
import matplotlib
import matplotlib.pyplot as plt
 
ACTIONS = ('forward', 'forwardLeft', 'forwardRight', 'backward', 'backRight', 'backwardLeft', 'stop')

df1 = pd.read_csv("dataset.csv", usecols=[1,4])
dataset = np.array(df1)

X = []
y = dataset[:,1]

batch_size = 128
epochs = 12
img_rows = 240
img_cols = 320

input_size = img_rows*img_cols
input_shape = (input_size,)

y = np.array(y)
num_classes = len(set(y))

y_freq = {}
for value in y:
    if y_freq.get(value) == None:
        y_freq[value] = 0
    y_freq[value] += 1

max_data = min(y_freq.values())

limit_dataset = {}

# print input_shape
y = []

for data in dataset:
    target  = data[1]   

    if limit_dataset.get(target) in (max_data, ):
        continue

    image_path = data[0]
    image   = misc.imread(image_path, mode='L')
    image   = misc.imresize(image, 10) # 10%
    #cv2.imshow(target, image)
    #sleep(2)
    X.append(image)
    y.append(target)

    if limit_dataset.get(target) == None:
        limit_dataset[target] = 0
    limit_dataset[target] += 1

y = np.array(y)

X = np.array(X)
X = X.astype('float32')
X /= 255

y = y.reshape(y.shape[0], 1)


y = y.astype('float32')

y = to_categorical(y, num_classes)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

print X_train.shape
print X_test.shape
print X.shape

"""
model = Sequential()
model.add(Dense(32, activation='relu', input_shape=input_shape))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

history = model.fit(X_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(X_test, y_test)
                )
score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
"""

# Load the MNIST dataset from pre-inn chainer method
#train, test = chainer.datasets.get_mnist(ndim=1)
train = X 
y_classes = np.argmax(y, axis=1)

# ROW = 7
# COLUMN = 7
# for i in range(ROW * COLUMN):
#     # print i 
#     # print len(train)
#     if  i >= len(train):
#         break
#     # train[i][0] is i-th image data with size 28x28
#     image = train[i]   # not necessary to reshape if ndim is set to 2
#     plt.subplot(ROW, COLUMN, i+1)          # subplot with size (width 3, height 5)
#     #img = misc.imresize(image, 10) # 10%
#     plt.imshow(image, cmap='gray')  # cmap='gray' is for black and white picture.
#     # train[i][1] is i-th digit label
#     plt.title('{}'.format(ACTIONS[y_classes[i]]), fontsize=8)
#     plt.axis('off')  # do not show axis value

# #plt.tight_layout(pad=0.1, w_pad=0.1, h_pad=0.1)
# #plt.savefig('dataset_plot.png')
# #plt.show()

X = X.reshape(X.shape[0], X[0].shape[0] * X[0].shape[1])

# print X


from sklearn.neural_network import MLPClassifier
#for layer in range(15, 50):

scoring = 'accuracy'
model = MLPClassifier(hidden_layer_sizes=(32), verbose=True, random_state=1)
model.fit(X, y)

print model.classes_

y_pred = model.predict(X)
y_pred = np.argmax(y_pred, axis=1)


print model.score(X, y)

y1 = np.argmax(y, axis=1)
print confusion_matrix(y1, y_pred)

#kfold = model_selection.KFold(n_splits=10, random_state=1)
#cv_results = model_selection.cross_val_score(model, X, y, cv=kfold, scoring=scoring)

#print cv_results
#msg = "Mean: %f (%f)" % (cv_results.mean(), cv_results.std())
#print(msg)

#print model.

#print model.score(X_test, y_test)


import pickle
output_file = open('model.pickle', 'wb')
pickle.dump(model, output_file)
output_file.close()

input_file = open('model.pickle', 'rb')
clf = pickle.load(input_file)
print clf.score(X, y)
#s.save()
# clf2 = pickle.loads(s)

"""
[ 0.95454545  0.86363636  0.84090909  0.97727273  1.          0.81818182
  1.          0.97674419  0.76744186  0.86046512]
Mean: 0.905920 (0.080702)
"""