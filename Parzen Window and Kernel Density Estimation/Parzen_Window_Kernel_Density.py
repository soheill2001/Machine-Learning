import csv
from numpy import exp, pi, sqrt
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity

DATA_PATH = 'ted_main.csv'

def Read_CSV(data_path):
    File = open(data_path, encoding = 'cp850')
    csvreader = csv.reader(File)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(float(row[2]))
    return rows

def Gaussian(x):
    return (1 / (sqrt(2 * pi))) * exp((-0.5) * (x**2))

def Parzen_Window(Data, h, x):
    n = len(Data)
    Vn = h
    Const = 1 / (n * Vn)
    X = []
    for j in x:
        Pn = 0
        for i in range(n):
            Pn += Gaussian((j - Data[i]) / h)
        X.append(Const * Pn)
    return X

h = [10, 20, 50, 100]
x = np.arange(2000)
Durations = Read_CSV(DATA_PATH)
for i in range(250, len(Durations), 250):
    Duration = Durations[:i]
    Duration = np.array(Duration)
    Duration.sort()
    Window = KernelDensity(kernel = "gaussian", bandwidth = 10)
    Window.fit(Duration.reshape(-1, 1))
    plt.plot(Duration, np.exp(Window.score_samples(Duration.reshape(-1, 1))))
plt.xlim([0, 2000])
plt.title("With Library")
plt.show()
for i in h:
  X = Parzen_Window(Durations, i, x)
  plt.legend('{}'.format(i))
  plt.plot(x, X)
plt.title("Without Library")
plt.show()