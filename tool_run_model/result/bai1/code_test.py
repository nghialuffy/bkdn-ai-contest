import pickle
import sys
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
model = pickle.load(open("model.pkl", "rb"))
import numpy as np
import pandas as pd
inp = sys.stdin.read()
inp = np.array([inp.split(",")])
inp = pd.DataFrame(inp, columns = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'])
# print(type(inp))

# test_X = iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] # taking test data feature
prediction = model.predict(inp)
# print(list(prediction))
[print(x) for x in list(prediction)]