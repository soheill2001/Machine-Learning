import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def Classifier(x_train, y_train, x_test, y_test, x_valid, y_valid, SOLVER, LEARNING, LAYERS, LAYERS_W):
    if SOLVER == 'sgd' or SOLVER == 'adam':
        clf = MLPClassifier(solver = SOLVER, learning_rate = "constant", learning_rate_init = LEARNING, hidden_layer_sizes = (LAYERS_W, LAYERS))
        clf.fit(x_train, y_train)
        plt.plot(clf.loss_curve_)
        plt.title("Train loss: solver:{} learning_rate:{} layerrs:{} layers_weight:{}".format(SOLVER, LEARNING, LAYERS, LAYERS_W))
        #plt.show()
        clf.fit(x_valid, y_valid)
        plt.plot(clf.loss_curve_)
        #plt.title("Validation loss: solver:{} learning_rate:{} layerrs:{} layers_weight:{}".format(SOLVER, LEARNING, LAYERS, LAYERS_W))
        plt.legend(["train", "test"])
        plt.show()
        ypred = clf.predict(x_test)
        return accuracy_score(y_test, ypred)
    else:
        clf = MLPClassifier(solver = SOLVER, learning_rate = LEARNING, hidden_layer_sizes = (LAYERS_W, LAYERS))
        clf.fit(x_train, y_train)
        plt.plot(clf.loss_curve_)
        plt.title("Train loss: solver:{} learning_rate:{} layerrs:{} layers_weight:{}".format(SOLVER, LEARNING, LAYERS, LAYERS_W))
        #plt.show()
        clf.fit(x_valid, y_valid)
        plt.plot(clf.loss_curve_)
        #plt.title("Validation loss: solver:{} learning_rate:{} layerrs:{} layers_weight:{}".format(SOLVER, LEARNING, LAYERS, LAYERS_W))
        plt.legend(["train", "test"])
        plt.show()
        ypred = clf.predict(x_test)
        return accuracy_score(y_test, ypred)

x_train = pd.read_csv('fashion-mnist_train.csv')
y_train = x_train['label']
del x_train['label']
x_test = pd.read_csv('fashion-mnist_test.csv')
y_test = x_test['label']
del x_test['label']
x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size = 0.1)

layers = [1, 2]
layers_w = [100]
solvers = ['sgd', 'adam', 'lbfgs']
learning_rate = [0.1]

for i in layers:
    for j in layers_w:
        for k in solvers:
            for z in learning_rate:
                print(Classifier(x_train, y_train, x_test, y_test, x_valid, y_valid, k, z, i, j))