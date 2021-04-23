import pickle
import sys
model = pickle.load(open("model.pkl", "rb"))

import pandas as pd
print(sys.argv[1])
iris = pd.read_csv(sys.argv[1])
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
test_X = iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] # taking test data feature
prediction = model.predict(test_X)
# print(list(prediction))
[print(x) for x in list(prediction)]