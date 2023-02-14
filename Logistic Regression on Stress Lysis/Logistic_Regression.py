import csv
import matplotlib.pyplot as plt
import random
import math
import numpy as np
import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn import metrics

DATA_PATH = "Stress-Lysis.csv"
CONFUSION_MATRIX = "Confusion_Matrix:"
ACCURACY = "Accuracy ="
TRAIN_TEST_THRESHOLD = 0.8
ETTA = 0.0000001

def Read_CSV(data_path):
    File = open(data_path)
    csvreader = csv.reader(File)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    for i in range(len(rows)):
        for j in range(len(rows[i]) - 1):
            rows[i][j] = float(rows[i][j])
    return rows

def Split_Data_To_Train_Test(data):
    random.shuffle(data)
    train_data = data[:math.floor(len(data) * TRAIN_TEST_THRESHOLD)]
    test_data = data[math.floor(len(data) * TRAIN_TEST_THRESHOLD):]
    return train_data, test_data

def Graph_Datas(data):
    ax = plt.gca()
    for i in range(2):
        X_low = []
        Y_low = []
        X_mid = []
        Y_mid = []
        X_high = []
        Y_high = []
        for j in range(i,2,1):
            for k in range(len(data)):
                if data[k][-1] == "low":
                    X_low.append(datas[k][i])
                    Y_low.append(datas[k][j + 1])
                elif data[k][-1] == "mid":
                    X_mid.append(datas[k][i])
                    Y_mid.append(datas[k][j + 1])
                else:
                    X_high.append(datas[k][i])
                    Y_high.append(datas[k][j + 1])
        ax.scatter(X_low, Y_low, color = "g")
        ax.scatter(X_mid, Y_mid, color = "b")
        ax.scatter(X_high, Y_high, color = "r")
        plt.show()

def Sigmoid(z):
    z = np.array(z)
    return 1 / (1 + np.exp(-z))

def Gradient_Descent(data, Label):
    W = [0] * 2
    W = np.matrix(W)
    W = np.transpose(W)
    for i in range(200):
        Sum = 0
        for j in range(len(data)):
            temp = [data[j][0], data[j][1]]
            temp = np.matrix(temp)
            temp = np.transpose(temp)
            k = np.dot(np.transpose(W), temp)
            if data[j][-1] == Label:
                Sum += np.dot(temp, (1 - Sigmoid(k)))
            else:
                Sum += np.dot(temp, (0 - Sigmoid(k)))
        W = W + (ETTA * Sum)
    return W

def Predict(data, W):
    Predict_Low = 0
    Predict_Mid = 0
    Predict_High = 0
    Predict = []
    for i in range(len(data)):
        temp = [data[i][0], data[i][1]]
        temp = np.matrix(temp)
        temp = np.transpose(temp)
        probabilities = []
        for j in W:
            probabilities.append(Sigmoid(np.dot(np.transpose(j), temp)))
        if probabilities[0] == max(probabilities):
            Predict.append("low")
            if data[i][-1] == "low":
                Predict_Low += 1
        if probabilities[1] == max(probabilities):
            Predict.append("mid")
            if data[i][-1] == "mid":
                Predict_Mid += 1
        if probabilities[2] == max(probabilities):
            Predict.append("high")
            if data[i][-1] == "high":
                Predict_High += 1
    print(ACCURACY, (Predict_Low + Predict_High + Predict_Mid) / len(data))
    return Predict

datas = Read_CSV(DATA_PATH)
Graph_Datas(datas)
Data_Train, Data_Test = Split_Data_To_Train_Test(datas)
W_Low = Gradient_Descent(Data_Train, "low")
W_Mid = Gradient_Descent(Data_Train, "mid")
W_High = Gradient_Descent(Data_Train, "high")
Y_Predict = Predict(Data_Test, [W_Low, W_Mid, W_High])

A = [0] * 2
B = [0]
B = np.array(B)
A = np.array(A)
for i in range(len(Data_Train)):
    temp = []
    temp2 = []
    temp2.append(Data_Train[i][-1])
    for j in range(2):
        temp.append(Data_Train[i][j])
    temp = np.array(temp)
    temp2 = np.array(temp2)
    B = np.vstack((B, temp2))
    A = np.vstack((A, temp))
A = np.delete(A, 0, 0)
B = np.delete(B, 0, 0)

C = [0] * 2
D = [0]
D = np.array(D)
C = np.array(C)
for i in range(len(Data_Test)):
    temp = []
    temp2 = []
    temp2.append(Data_Test[i][-1])
    for j in range(2):
        temp.append(Data_Test[i][j])
    temp = np.array(temp)
    temp2 = np.array(temp2)
    D = np.vstack((D, temp2))
    C = np.vstack((C, temp))
C = np.delete(C, 0, 0)
D = np.delete(D, 0, 0)

print(metrics.confusion_matrix(D, Y_Predict))

clf = OneVsRestClassifier(SVC()).fit(A, B)
print(clf.score(C,D))
