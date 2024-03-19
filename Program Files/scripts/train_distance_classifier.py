from DUQ330BIGDATA.Week5 import distance_classifier, distances, npi_grants_combine
from DUQ330BIGDATA.Week6 import data_simulator
import pandas as pd

#Obtaining data using npi_grants_combine reacer file
data = npi_grants_combine.read(r"data/npidata_pfile_20240205-20240211.csv")

#Making training data by instantiating NameDistance Class and making features
nd = distances.NameDistance()
df = nd.training_data(data)

#Making a training dataset from my simulated training data
df2 = nd.training_data(data_simulator.df)

#Creating a classifier
dc = distance_classifier.DistanceClassifier(r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\DUQ330BIGDATA\Week6", 'data')

#Training and saving the model
dc.train(df2, data_simulator.df['label'])
dc.save('distance_classifier')