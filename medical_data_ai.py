#medical data
#predict people that have diabetes, from this
#attributes [smoker, overweight, ethnicity, etc]
#output results
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_validate
import pandas as pd

#Generate data
# file = 'medical_data.csv'
# test_df = pd.read_csv(file)
# print(test_df)

#Training data | separate features, labels
file = 'cardio_train.csv'
training_df = pd.read_csv(file,sep = ';')
# print(training_df)

labels = training_df.iloc[:, -1:]
print(labels)
features = training_df.iloc[:, : -1]
print(features)
classifier = DecisionTreeClassifier()
classifier.fit(features,labels)

scoring = ['precision_macro', 'recall_macro', 'f1_macro']

#Data validation settings
scores = cross_validate(classifier, features, labels, cv = 5, scoring = scoring)

#Accuracy in training, divides data up into 5 pieces.
#Recall 2nd 5th.
#F1 score, precision * recall + precision + recall
print(f"Precision: {scores['test_precision_macro']} \n'Recall': {scores['test_recall_macro']} \n'F1 Score': {scores['test_f1_macro']} \n")
# print(classifier.predict([[0, 18393, 2, 168, 62.0, 110, 80, 1, 1, 0, 0, 1]]))

#temp storage 0;18393;2;168;62.0;110;80;1;1;0;0;1;0