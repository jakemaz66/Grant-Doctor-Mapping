from program_files.distance_classifier import distance_classifier, name_distance
from program_files import npi_grants_combine

#Loading reusable classifier 
model = distance_classifier.DistanceClassifier(r'C:\Users\jakem\Grant-Doctor-Mapping-1\program_files\trained_model', 'xgb')

#Loading in the trained model, trained using 'train_distance_classifier' script
model.load('distance_classifier.json')

#Creating test data by combining data frames
test_data = npi_grants_combine.read(r"C:\Users\jakem\Grant-Doctor-Mapping-1\program_files\data\npidata_pfile_20240205-20240211.csv")

#Taking the first 100 rows
test_data = test_data.iloc[0:100]

#Extracting the distance features from the test data using the 'training_data' method within the NameDistance class
features = name_distance.NameDistance().training_data(test_data)

#Collecting predictions, setting proba to true to get probabilities
preds = model.predict(features, proba=True)

test_data

