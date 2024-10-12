import pandas as pd

df = pd.read_csv('tennis_data.txt',header=None)
df.columns = ['ID','outlook', 'temp', 'humidity', 'wind','play']

hot_no = len(df[(df['temp']=='Hot') & (df['play']=='No')]) / len(df[df['play']=='No'])
mild_no = len(df[(df['temp']=='Mild') & (df['play']=='No')]) / len(df[df['play']=='No'])
cool_no = len(df[(df['temp']=='Cool') & (df['play']=='No')]) / len(df[df['play']=='No'])
hot_yes = len(df[(df['temp']=='Hot') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])
mild_yes = len(df[(df['temp']=='Mild') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])
cool_yes = len(df[(df['temp']=='Cool') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])

print(hot_no, hot_yes, mild_no, mild_yes, cool_no, cool_yes)

sunny_no = len(df[(df['outlook']=='Sunny') & (df['play']=='No')]) / len(df[df['play']=='No'])
overcast_no = len(df[(df['outlook']=='Overcast') & (df['play']=='No')]) / len(df[df['play']=='No'])
rain_no = len(df[(df['outlook']=='Rain') & (df['play']=='No')]) / len(df[df['play']=='No'])
sunny_yes = len(df[(df['outlook']=='Sunny') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])
overcast_yes = len(df[(df['outlook']=='Overcast') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])
rain_yes = len(df[(df['outlook']=='Rain') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])

print(sunny_no, overcast_no, rain_no, sunny_yes, overcast_yes, rain_yes)

strong_no = len(df[(df['wind']=='Strong') & (df['play']=='No')]) / len(df[df['play']=='No'])
weak_no = len(df[(df['wind']=='Weak') & (df['play']=='No')]) / len(df[df['play']=='No'])
strong_yes = len(df[(df['wind']=='Strong') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])
weak_yes = len(df[(df['wind']=='Weak') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])

print(strong_no, weak_no, strong_yes, strong_no)

high_no = len(df[(df['humidity']=='High') & (df['play']=='No')]) / len(df[df['play']=='No'])
normal_no = len(df[(df['humidity']=='Normal') & (df['play']=='No')]) / len(df[df['play']=='No'])
high_yes = len(df[(df['humidity']=='High') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])
normal_yes = len(df[(df['humidity']=='Normal') & (df['play']=='Yes')]) / len(df[df['play']=='Yes'])

print(high_no, high_yes, normal_no, normal_yes)