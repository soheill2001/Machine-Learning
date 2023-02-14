# Clustering Emotion Data using various clustering algorithms

This code implements five clustering algorithms, including DBSCAN, HDBSCAN, KMeans, GMM, and Agglomerative Clustering. It also uses a dataset of features, emotions, genders, and text IDs, where the features are extracted from the text using BERT pre-trained embeddings.

The code starts with loading the data into the numpy arrays. Then, it finds the best epsilon value for the DBSCAN algorithm using the knee method. After that, the code implements the DBSCAN algorithm with the best epsilon value to cluster the data. The code also shows the result of HDBSCAN, KMeans, GMM, and Agglomerative Clustering algorithms with different numbers of clusters.

### DBSCAN Algorithm
The DBSCAN algorithm is used to cluster the data with a best epsilon value of 33 and minimum samples of 124.

### HDBSCAN Algorithm
The HDBSCAN algorithm is used with various minimum cluster sizes, including 2, 4, and 10.

### KMeans Algorithm
The KMeans algorithm is used with various numbers of clusters, including 2, 4, and 10.

### GMM Algorithm
The GMM algorithm is used with various numbers of clusters, including 2, 4, and 10.

## Prerequisites
The project requires the following libraries:
```
NumPy
Pandas
Matplotlib
Scikit-Learn
hdbscan
kneed
```
The output of each algorithm is a scatter plot of the clustering results, where each cluster is represented by a different color. The plots can help visualize the differences in the clustering results of different algorithms. The input data should be in csv format.

To run the code, you can simply execute the code cells in a Jupyter notebook or any other compatible environment.
