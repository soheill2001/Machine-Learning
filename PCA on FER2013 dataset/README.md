# Facial Expression Recognition using PCA and KNN
This repository contains a Python implementation of facial expression recognition using Principal Component Analysis (PCA) and K-Nearest Neighbors (KNN). The implementation is based on the FER2013 dataset, which is a popular dataset for facial expression recognition.
## Requirements
The implementation requires the following packages to be installed:

+ pandas
+ numpy
+ scikit-learn
+ matplotlib
These packages can be installed via pip.
## Usage
To run the implementation, you can simply run the Facial_Expression_Recognition.ipynb notebook.

The notebook contains three main parts:

### Data Loading and Preprocessing
In this section, the FER2013 dataset is loaded, and the images are preprocessed to be ready for feature extraction using PCA.

### Feature Extraction using PCA
In this section, the eigenvalues and eigenvectors are computed for the preprocessed images, and the images are projected onto the eigenvectors to obtain a lower-dimensional feature representation.

### Facial Expression Recognition using KNN
In this section, a KNN classifier is trained on the lower-dimensional feature representations obtained from PCA, and the accuracy of the classifier is evaluated.

## Results
The implementation achieves a recognition accuracy of 60.05% on the test set using the full feature space. By reducing the feature space to the top 4 eigenvectors, the accuracy drops to 49.59%. The recognition accuracy is found to increase as more eigenvectors are used, up to a limit of around 30-40 eigenvectors.