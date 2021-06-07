import pandas as pd
iris = pd.read_csv('Iris.csv')

import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

train, test = train_test_split(iris, test_size = 0.3)

train_X = train[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] # taking the training data features
train_y = train.Species # output of the training data

test_X = test[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] # taking test data feature
test_y = test.Species # output value of the test data
model  = LogisticRegression()
model.fit(train_X, train_y)
prediction = model.predict(test_X)
print('The accuracy of Logistic Regression is: ', accuracy_score(prediction, test_y))
with open('model.pkl', 'wb') as out:
    pickle.dump(model, out, protocol=pickle.HIGHEST_PROTOCOL)
