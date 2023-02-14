# Cancer Patient Classifier
This is a Python program that estimates the accuracy of a cancer patient classifier using k-fold cross-validation. The program reads a CSV file containing data about cancer patients, handles missing data, extracts the actual answers, and estimates the accuracy of a voting classifier using k-fold cross-validation.
## Requirements
This program requires the following libraries to be installed:

+ scikit-learn
+ numpy
+ pandas
+ matplotlib
## Usage
To use this program, put your cancer patient data in a CSV file with the following format:
```
attr1,attr2,attr3,...,attrN,class
val11,val12,val13,...,val1N,class1
val21,val22,val23,...,val2N,class2
...
valM1,valM2,valM3,...,valMN,classM
```
Note that class is the target variable, which must be binary (0 or 1). Any missing data should be replaced by ?.


The program will output the estimated accuracy of the cancer patient classifier using k-fold cross-validation.