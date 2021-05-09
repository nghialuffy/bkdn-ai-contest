import pickle
model = pickle.load( open( "model.pkl", "rb" ) )

import pandas as pd
iris = pd.read_csv('test.csv')

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

test_X = iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] # taking test data feature
test_y = iris.Species
prediction = model.predict(test_X)
print('The accuracy of Logistic Regression is: ', accuracy_score(prediction, test_y))