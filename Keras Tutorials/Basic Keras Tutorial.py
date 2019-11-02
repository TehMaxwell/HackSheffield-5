# -*- coding: utf-8 -*-
"""
This is the basic tutorial for running Keras with Tensorflow using Python.
"""
#MODULES
import pandas
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy
from keras.models import Sequential
from keras.layers import Dense

#DEFINITIONS
redWine = r"http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
whiteWine = r"http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
EPOCHS = 20

#MAIN CODE
#Importing the Red and White Wine Data
whiteWineData = pandas.read_csv(whiteWine, sep = ";")
redWineData = pandas.read_csv(redWine, sep = ";")

#Adding a wine type column to allow for the datasets to be combined
whiteWineData["type"] = 1
redWineData["type"] = 0

#Appending the Red Wine Data to the White Wine Data
wineData = redWineData.append(whiteWineData, ignore_index = True)

#Pulling X and Y Axis data from the DataFrame
X = wineData.ix[:, 0:11]
y = numpy.ravel(wineData.type)

#Splitting the Data into a Training and Testing set
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

#Scaling the data accordingly
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#Generating the neural network model
NN = Sequential()
NN.add(Dense(12, activation = "relu", input_shape = (11, )))
NN.add(Dense(8, activation = "relu"))
NN.add(Dense(1, activation = "sigmoid"))

#Showing the shape and summary of the model
NN.output_shape
NN.summary()

#Fitting the Model
NN.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
NN.fit(X_train, Y_train, epochs=EPOCHS, batch_size=1, verbose=1)

#Generating Predictions
evaluation = NN.evaluate(X_test, Y_test)
print(evaluation)
