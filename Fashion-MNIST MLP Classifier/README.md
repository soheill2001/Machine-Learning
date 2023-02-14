# Fashion-MNIST MLP Classifier
This project contains a Python script that trains and tests a multilayer perceptron (MLP) model on the Fashion-MNIST dataset using the scikit-learn library. The Fashion-MNIST dataset contains images of different clothing items and is a popular benchmark dataset for image classification tasks.

The Classifier function in the mlp_classifier.py script takes in the training and test data, along with various hyperparameters for the MLP model, and returns the accuracy of the model on the test data. It also plots the loss curve for the training and validation data.

The hyperparameters that can be tuned include the solver (SGD, Adam, or L-BFGS), the learning rate, the number of layers, and the number of neurons in each layer. The script includes a loop that tests the model on different combinations of these hyperparameters and prints the accuracy for each combination.

## Requirements
The script requires the following packages:
```
numpy
pandas
scikit-learn
matplotlib
```
These packages can be installed using pip.


## Usage
To use the script, download the Fashion-MNIST dataset in CSV format from Kaggle and place the `fashion-mnist_train.csv` and `fashion-mnist_test.csv` files in the same directory as the `mlp_classifier.py` script.

The script will output the accuracy for each combination of hyperparameters that it tests.