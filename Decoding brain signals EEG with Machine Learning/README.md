# EEG Signal Classification: Piano vs Face
This code uses EEG signals to classify whether a person is looking at a piano or a face image. The data consists of EEG signals recorded while a person looked at piano and face images.
The following machine learning algorithms have been used in this code:

+ Logistic Regression
+ Support Vector Machine (SVM)
+ Decision Tree
+ K-Nearest Neighbors (KNN)
+ Multi-Layer Perceptron (MLP)
## Dependencies
```
scipy
numpy
sklearn
matplotlib
mne
```
These dependencies can be installed using pip.

## Data
The data used in this code is contained in two .mat files: S2T2B1.mat and S2T2B2.mat. The data in both files has been preprocessed and is ready for classification. The Read_data function reads both .mat files and returns the data and labels as numpy arrays. The Shuffle function shuffles the data and labels to ensure the data is well mixed.

## Algorithms
### Logistic Regression
Logistic regression is a linear model used for binary classification. In this code, the logistic regression algorithm is used to classify the piano and face data.

### Support Vector Machines
Support vector machines (SVM) are a popular class of algorithms used for classification. In this code, SVM with the radial basis function kernel is used to classify the piano and face data.

### Decision Tree
Decision trees are a popular machine learning algorithm used for classification. In this code, a decision tree classifier is used to classify the piano and face data.

### K-Nearest Neighbor
K-nearest neighbor (KNN) is a classification algorithm that is based on the distance between samples. In this code, KNN is used to classify the piano and face data.

### Multilayer Perceptron
Multilayer perceptron (MLP) is a neural network that is commonly used for classification problems. In this code, an MLP classifier is used to classify the piano and face data.

## Running the code
After installing the required dependencies, run the code using a Python interpreter. The code outputs graphs showing the accuracy of the classification for each algorithm. The graphs show the accuracy over time, with a smooth curve overlaid on the original curve to make it easier to read.

Note that the SlidingEstimator class from the mne.decoding package is used to compute the accuracy over time. This class uses a sliding window to obtain the accuracy at each time point. The window size can be adjusted by changing the n_jobs parameter.
