import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
import pandas as pd

# Loading Data using pandas
Data = pd.read_csv(r"Personality_Test.csv")

# Data features
X = Data.iloc[:, 1:17]
# Data targets
Y = Data.iloc[:, 0:1]

# Spliting the Data to train and test
x_train, x_test, y_train, y_test = train_test_split(X, Y)
# flattening training target to avoid errors
y_train = y_train.values
y_train = y_train.flatten()

# Using neural network
Classifier = MLPClassifier(hidden_layer_sizes=[
                           200, 200], activation='identity', solver='sgd', max_iter=1000, shuffle=True, learning_rate_init=0.1)

# Training
Classifier.fit(x_train, y_train)
# Testing
y_pred = Classifier.predict(x_test)
# Accuracy test
acc = int(accuracy_score(y_test, y_pred)*100)
print("The Accuracy Is ", acc, '%', sep='')
