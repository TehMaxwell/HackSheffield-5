# -*- coding: utf-8 -*-
"""
This is the code for training a Neural Network to play the game Blackjack.
This NN is being generated based upon a prexisting Blackjack Dataset.
"""
#MODULES
import numpy
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

#DEFINTIONS
blackJackDataFile = "blkjckhands.csv"

numberOfHands = 20000
EPOCHS = 20

#MAIN CODE
#Generating a random array of blackjack hands
randomHands = numpy.random.randint(2, high = 20, size = numberOfHands)
randomTwists = numpy.random.randint(1, high = 11, size = numberOfHands)

#Generating an array of Training Data
shouldTwist = numpy.where(randomHands + randomTwists <= 21, 1, 0)

#Splitting the data into training and test data
X_train, X_test, Y_train, Y_test = train_test_split(randomHands, shouldTwist, test_size = 0.33, random_state = 42)

#Generating the Neural Network
NN = Sequential()
NN.add(Dense(1, activation = "relu", input_shape = (1, )))
NN.add(Dense(6, activation = "relu"))
NN.add(Dense(6, activation = "relu"))
NN.add(Dense(1, activation = "sigmoid"))

#Compiling Neural Network
NN.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
NN.fit(X_train, Y_train, epochs=EPOCHS, batch_size=1, verbose=1)

#Generating Predictions
evaluation = NN.evaluate(X_test, Y_test)
print(evaluation)