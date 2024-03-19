from program_files.distance_classifier import data_simulator, distance_classifier, name_distance
import pandas as pd
from program_files import npi_grants_combine

#Obtaining data using npi_grants_combine reacer file
data = npi_grants_combine.read(r"C:\Users\jakem\Grant-Doctor-Mapping-1\program_files\data\npidata_pfile_20240205-20240211.csv")

#Making training data by instantiating NameDistance Class and making features
nd = name_distance.NameDistance()
df = nd.training_data(data)

#Making a training dataset from my simulated training data
sim_data = data_simulator.create_simulated_data()
df2 = nd.training_data(sim_data)

#Creating a classifier
dc = distance_classifier.DistanceClassifier(r"C:\Users\jakem\Grant-Doctor-Mapping-1\program_files\trained_model", 'data')

#Training and saving the model
dc.train(df2, sim_data['label'])
dc.save('distance_classifier')