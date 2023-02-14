# Decision Tree on Restaurant Dataset
This code is an implementation of the decision tree algorithm in Python. It uses the following algorithm to generate a decision tree from a given dataset:

1. Calculate the entropy of the dataset.
2. For each attribute/feature:
  - a. Calculate the entropy of the attribute.
  - b. Calculate the information gain of the attribute.
3. Choose the attribute with the highest information gain.
4. Add a node to the tree with the chosen attribute.
5. Create a branch for each possible value of the attribute.
6. Repeat the process for each branch, recursively, until the leaves of the tree are pure or no more features remain to be selected.
## Requirements
This code requires Python 3.x to be installed on your system.
## Dataset
The dataset used in this code is a restaurant dataset with 12 attributes and 12 instances. The dataset contains information about the restaurant, such as the type of cuisine, the price range, and the weather conditions. The goal of the algorithm is to predict whether a customer will wait for a table at the restaurant or not, based on the attributes provided.
