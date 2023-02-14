import csv
import random
import math
import numpy as np

DATA_PATH = "Iris.csv"
CONFUSION_MATRIX = "Confusion_Matrix:"
ACCURACY = "Accuracy ="
TRAIN_TEST_THRESHOLD = 0.7

def Read_CSV(data_path):
    File = open(data_path)
    csvreader = csv.reader(File)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    return rows

def Split_Data_To_Train_Test(data):
    random.shuffle(data)
    train_data = data[:math.floor(len(data) * TRAIN_TEST_THRESHOLD)]
    test_data = data[math.floor(len(data) * TRAIN_TEST_THRESHOLD):]
    return train_data, test_data

def Train_Data_Classification_By_Class(data):
    data_class = dict()
    for i in range(len(data)):
        row_data = data[i]
        if row_data[-1] not in data_class:
            data_class[row_data[-1]] = list()
        data_class[row_data[-1]].append(row_data)
    return data_class

def Calculate_Mean(data):
    parameters = len(data[0]) - 1
    Mean = [0] * parameters
    for i in range(len(data)):
        for j in range(parameters):
            Mean[j] += float(data[i][j])
    Mean[:] = [x / len(data) for x in Mean]
    return Mean

def Calculate_Variance(data, Mean):
    parameters = len(data[0]) - 1
    Variance = [0] * parameters
    for i in range(len(data)):
        for j in range(parameters):
            Variance[j] += (float(data[i][j]) - Mean[j]) ** 2
    Variance[:] = [math.sqrt(x / (len(data) - 1)) for x in Variance]
    return Variance

def Calculate_Mean_Variance_For_Each_Class(data):
    statistics = dict()
    for key in data.keys():
        Mean = Calculate_Mean(data[key])
        Variance = Calculate_Variance(data[key], Mean)
        statistics[key] = [Mean, Variance]
    return statistics

def Calculate_Probability(data, Mean, Variance):
    exponent = math.exp( -0.5 * ((data - Mean) ** 2 / (Variance ** 2)))
    probability = (1 / (math.sqrt(2 * math.pi) * Variance)) * exponent
    return probability
 
def Predict(data, parameters):
    probability_class = dict()
    for i in parameters.keys():
        for j in range(len(parameters[i][0])):
            if i not in probability_class:
                probability_class[i] = 1
            probability_class[i] *= Calculate_Probability(float(data[j]), parameters[i][0][j], parameters[i][1][j])
    return max(probability_class, key = probability_class.get)

def Creat_Hash_Table(parameters):
    hash_table = dict()
    i = 0
    for key in parameters.keys(): 
        hash_table[key] = i
        i += 1
    return hash_table

def Print_Results(Confusion_Matrix):
    print(CONFUSION_MATRIX + "\n", Confusion_Matrix)
    Sum_true = 0
    Sum_all = 0
    for i in range(len(Confusion_Matrix)):
        Sum_true += Confusion_Matrix[i][i]
        Sum_all += sum(Confusion_Matrix[i])
    print(ACCURACY, Sum_true / Sum_all)

data = Read_CSV(DATA_PATH)
train_data, test_data = Split_Data_To_Train_Test(data)
train_data = Train_Data_Classification_By_Class(train_data)
class_parameters = Calculate_Mean_Variance_For_Each_Class(train_data)
hash_table = Creat_Hash_Table(class_parameters)
Confusion_Matrix = np.zeros((len(class_parameters), len(class_parameters)))
for i in range(len(test_data)):
    predict_test_data = Predict(test_data[i], class_parameters)
    Confusion_Matrix[hash_table[predict_test_data]][hash_table[test_data[i][-1]]] += 1
Print_Results(Confusion_Matrix)
