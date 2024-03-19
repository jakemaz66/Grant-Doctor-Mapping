from distance_classifier import data_simulator, distance_classifier, name_distance
import pandas as pd
import npi_grants_combine

#Obtaining data using npi_grants_combine reacer file
data = npi_grants_combine.read(r"data/npidata_pfile_20240205-20240211.csv")

#Making training data by instantiating NameDistance Class and making features
nd = name_distance.NameDistance()
df = nd.training_data(data)

#Making a training dataset from my simulated training data
df2 = nd.training_data(data_simulator.df)

#Creating a classifier
dc = distance_classifier.DistanceClassifier("trained_models", 'data')

#Training and saving the model
dc.train(df2, data_simulator.df['label'])
dc.save('distance_classifier')