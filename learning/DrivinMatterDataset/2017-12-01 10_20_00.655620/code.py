import pandas as pd
import numpy as np
from scipy import misc
import sys
import os

import keras
from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

import sys
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import model_selection

df1 = pd.read_csv("dataset.csv", usecols=[1,4])
dataset = np.array(df1)

X = []
y = [] #dataset[:,1]

batch_size = 128
epochs = 12
img_rows = 240
img_cols = 320

input_size = img_rows*img_cols
input_shape = (input_size,)

print input_shape

for data in dataset:
    if data[1] != "stop":
        image_path = data[0]
        X.append(misc.imread(image_path, mode='L'))
        y.append(data[1])

y = np.array(y)
num_classes = len(set(y))

X = np.array(X)
X = X.astype('float32')
X = X.reshape(X.shape[0], input_shape[0])
X /= 255

#print y
y = preprocessing.LabelEncoder().fit_transform(y)

#print y 

y = y.reshape(y.shape[0], 1)
y = y.astype('float32')
y = keras.utils.to_categorical(y, num_classes)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

print X.shape
print y.shape

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

from sklearn.neural_network import MLPClassifier
#for layer in range(15, 50):

scoring = 'accuracy'
#model = MLPClassifier(hidden_layer_sizes=(16), verbose=True, random_state=1)
#model.fit(X, y)

#kfold = model_selection.KFold(n_splits=10, random_state=1)
#cv_results = model_selection.cross_val_score(model, X, y, cv=kfold, scoring=scoring)

#print cv_results
#msg = "Mean: %f (%f)" % (cv_results.mean(), cv_results.std())
#print(msg)

#print model.score(X_test, y_test)

import pickle
#output_file = open('model.dat', 'wb')
#pickle.dump(model, output_file)
#output_file.close()

input_file = open('model.dat', 'rb')
clf = pickle.load(input_file)
print clf.score(X_test, y_test)
#s.save()
# clf2 = pickle.loads(s)