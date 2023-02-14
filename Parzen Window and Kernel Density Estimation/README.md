# Parzen Window and Kernel Density Estimation
This code implements the Parzen Window and Kernel Density Estimation methods to estimate the probability density function of a given dataset.
## Dependencies
This code requires the following dependencies:

+ csv
+ numpy
+ matplotlib
+ sklearn
## Usage
To use this code, follow these steps:

+ Make sure the required dependencies are installed.
+ Download the ted_main.csv file and save it in the same directory as the code.
+ Run the code.
The code will output two plots:

+ A plot of the probability density function estimated using the Kernel Density Estimation method, with the bandwidth set to 10.
+ A plot of the probability density function estimated using the Parzen Window method, with different bandwidth values.

## Functionality
The Read_CSV function reads the data from the ted_main.csv file and stores it in a list.

The Gaussian function returns the value of the Gaussian function for a given input.

The Parzen_Window function implements the Parzen Window method to estimate the probability density function for a given dataset. It takes the dataset, the bandwidth value, and an array of points at which to evaluate the density function as inputs, and returns an array of values corresponding to the density function evaluated at each point.

The KernelDensity class from the sklearn library is used to implement the Kernel Density Estimation method. The fit method is used to fit the data to the model, and the score_samples method is used to evaluate the probability density function at each point in the dataset.