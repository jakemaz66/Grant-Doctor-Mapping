from DUQ330BIGDATA.Week5 import distance_classifier, distances, npi_grants_combine
from DUQ330BIGDATA.Week5 import npi_grants_combine

#Loading reusable classifier 
model = distance_classifier.DistanceClassifier('DUQ330BIGDATA/Week6', 'xgb')
#Loading in the trained model, trained using 'train_distance_classifier' script
model.load('distance_classifier.json')

#Creating test data by combining data frames
test_data = npi_grants_combine.read(r"data/npidata_pfile_20240205-20240211.csv")
#Taking the first 100 rows
test_data = test_data.iloc[0:100]

#Extracting the distance features from the test data using the 'training_data' method within the NameDistance class
features = distances.NameDistance().training_data(test_data)

#Collecting predictions, setting proba to true to get probabilities
preds = model.predict(features, proba=True)

test_data

