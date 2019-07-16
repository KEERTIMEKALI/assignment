import pandas as pd

university = {'Name': ['Tom', 'nick', 'krish', 'jack','Mary','Jill','Harry','Potter','Ron','Daniel'],
              'USN': [1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019],
              'Sem': [6, 8, 4, 3, 8, 6, 1, 6, 4, 7],
              'Branch': ['CSE', 'ISE','ECE', 'EEE', 'CIV', 'MECH','ISE','CSE', 'ISE','MECH'],
              'Score' : [98, 78, 60, 87, 76, 45, 82, 90, 92,  95],
              'Region' : ['BELAGAVI' , 'MYSORE' , 'BENGALURU' ,'KALBURGI', 'BELAGAVI' , 'MYSORE', 'BELAGAVI', 'BENGALURU','BELAGAVI','MYSORE']
              }

df = pd.DataFrame(university)

d=df.describe()
print("Description \n",d)

print("the student with maximum marks is ",df['Name'][df['Score']==df['Score'].max()])

x=df.groupby(['Sem']).groups
print("Group by sem \n",x)

r=df.groupby(['Region']).groups
print("Group by region \n",r)

df['Name']=df['Name'].str.capitalize()
print("Capitalized name \n",df['Name'])

print(df.rename(index={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j'}))