import pandas as pd

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

print("Play Tennis?")
print("Nope", len(df[df['play']=='No'])/14)
print("Yes", len(df[df['play']=='Yes'])/14)
print("Temp......")
print("Hot No", round(hot_no,1))
print("Mild No", round(mild_no,1))
print("Cool No", round(cool_no,1))
print("Hot yes", round(hot_yes,1))
print("Mild yes", round(mild_yes,1))
print("Cool yes", round(cool_yes,1))
print("Outlook..........")
print("Sun yes", round(sunny_yes,1))
print("Overcast yes", round(overcast_yes,1))
print("Rain yes", round(rain_yes,1))
print("Sun no", round(sunny_no,1))
print("Overcast no", round(overcast_no,1))
print("Rain no", round(rain_no,1))
print("Wind..........")
print("Strong yes", round(strong_yes,1))
print("Weak yes", round(weak_yes,1))
print("Strong no", round(strong_no,1))
print("weak no", round(weak_no,1))
print("Humidiy......")
print("High yes", round(high_yes,1))
print("Normal yes", round(normal_yes,1))
print("High no", round(high_no,1))
print("Normal no", round(normal_no,1))

answer_yes = sunny_yes * cool_yes * high_yes * strong_yes * play_yes
answer_no = sunny_no * cool_no * high_no * strong_no * play_no

print(answer_yes)
print(answer_no)