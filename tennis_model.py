import pandas as pd

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.estimators import ParameterEstimator



df = pd.read_csv('tennis_data.txt',header=None) # Read in Tennis.CSV with observations
df.columns = ['ID','outlook', 'temp', 'humidity', 'wind', 'play'] # Add Column Names

# Defining the model structure. We can define the network by just passing a list of edges.
model = BayesianNetwork([('Temp', 'Outlook'), ('Humidity', 'Outlook'), ('Outlook', 'Play'), ('Wind', 'Play')])

# Defining individual CPDs.
cpd_Temp = TabularCPD(variable='Temp', variable_card=2, values=(high_no, high_yes))
cpd_Hum = TabularCPD(variable='Humidity', variable_card=2, values=[[0.7], [0.3]])