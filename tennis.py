import pandas as pd

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD


df = pd.read_csv('tennis_data.txt',header=None) # Read in Tennis.CSV with observations
df.columns = ['ID','outlook', 'temp', 'humidity', 'wind', 'play'] # Add Column Names

play_no = len(df[df['play']=='No'])
play_yes = len(df[df['play']=='Yes'])

hot_no = len(df[(df['temp']=='Hot') & (df['play']=='No')]) / len(df[df['play']=='No']) # calculate Likelihood of Hot Tennis given P(B|A) 
mild_no = len(df[(df['temp']=='Mild') & (df['play']=='No')]) / len(df[df['play']=='No']) # Calc likelihood of Mile Tennis give P(B|A)
cool_no = len(df[(df['temp']=='Cool') & (df['play']=='No')]) / len(df[df['play']=='No']) # ibid...
hot_yes = len(df[(df['temp']=='Hot') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])
mild_yes = len(df[(df['temp']=='Mild') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])
cool_yes = len(df[(df['temp']=='Cool') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])

sunny_no = len(df[(df['outlook']=='Sunny') & (df['play']=='No')]) / len(df[df['play']=='No']) 
overcast_no = len(df[(df['outlook']=='Overcast') & (df['play']=='No')]) / len(df[df['play']=='No'])
rain_no = len(df[(df['outlook']=='Rain') & (df['play']=='No')]) / len(df[df['play']=='No'])
sunny_yes = len(df[(df['outlook']=='Sunny') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])
overcast_yes = len(df[(df['outlook']=='Overcast') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])
rain_yes = len(df[(df['outlook']=='Rain') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])

strong_no = len(df[(df['wind']=='Strong') & (df['play']=='No')]) / len(df[df['play']=='No'])
weak_no = len(df[(df['wind']=='Weak') & (df['play']=='No')]) / len(df[df['play']=='No'])
strong_yes = len(df[(df['wind']=='Strong') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])
weak_yes = len(df[(df['wind']=='Weak') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])

high_no = len(df[(df['humidity']=='High') & (df['play']=='No')]) / len(df[df['play']=='No'])
normal_no = len(df[(df['humidity']=='Normal') & (df['play']=='No')]) / len(df[df['play']=='No'])
high_yes = len(df[(df['humidity']=='High') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])
normal_yes = len(df[(df['humidity']=='Normal') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])

#print("Prob Temp Hot, Prior No - ", hot_no, "\nProb Temp Hot, Prior Yes - ", round(hot_yes,1), "\nProb Temp Mild, Prior No - ", 
#mild_no, "\nProb Temp Mild, Prior Yes - ", round(mild_yes,1), "\nProb Temp Cool, Prior No - ", cool_no, "\nProb Temp Cool, Prior Yes - ", 
#round(cool_yes,1))


# Defining the model structure. We can define the network by just passing a list of edges.
model = BayesianNetwork([('Temp', 'Outlook'), ('Humidity', 'Outlook'), ('Outlook', 'Play'), ('Wind', 'Play')])

# Defining individual CPDs.
cpd_Temp = TabularCPD(variable='Temp', variable_card=2, values=(high_no, high_yes))
cpd_Hum = TabularCPD(variable='Humidity', variable_card=2, values=[[0.7], [0.3]])