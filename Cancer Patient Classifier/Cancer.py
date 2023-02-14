from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.svm import SVC
import csv

DATA_PATH = "cancer.csv"
MISSING_DATA = '?'

def Mean(numbers):
    return sum(numbers) / len(numbers)

def Find_Missing_Data_Column(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == MISSING_DATA:
                return j

def Read_CSV(data_path):
    File = open(data_path)
    csvreader = csv.reader(File)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    for i in range(len(rows)):
        rows[i].pop(0)
        for j in range(len(rows[i])):
            if rows[i][j] != MISSING_DATA:
                rows[i][j] = int(rows[i][j])
    return rows

def Handle_Missing_Data(datas):
    Sum = []
    rows_with_missing_data = []
    missing_column = Find_Missing_Data_Column(datas)
    for i in range(len(datas)):
        if datas[i][missing_column] != MISSING_DATA:
            Sum.append(datas[i][missing_column])
        else:
            rows_with_missing_data.append(i)
    for i in rows_with_missing_data:
        datas[i][missing_column] = Mean(Sum)
    return datas

def Extract_Actual_Answer(datas):
    y_data = []
    for i in datas:
        y_data.append(i.pop(-1))
    return datas, y_data

def Estimate(datas, y_data):
    kfold = KFold(n_splits = 10)
    models = [('lr', LogisticRegression()), ('svm', SVC()), ('tree', DecisionTreeClassifier())]
    model = VotingClassifier(estimators = models)
    scores = cross_val_score(model, datas, y_data, scoring = 'accuracy', cv = kfold)
    print("accuracy:", Mean(scores) * 100)

datas = Read_CSV(DATA_PATH)
datas = Handle_Missing_Data(datas)
datas, y_data = Extract_Actual_Answer(datas)
Estimate(datas, y_data)