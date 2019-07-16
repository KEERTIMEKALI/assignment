import pandas as pd
df=pd.read_csv("C:\\Users\\HP\\Desktop\\jac.csv")
print(df)

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