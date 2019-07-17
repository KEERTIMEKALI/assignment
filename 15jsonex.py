'''import pandas as pd

data =[
    {
        "textbookname":"DBMS",
        "author name" :"Navthy",
        "age":"89"
    },
   {
        "textbookname": "C++",
        "author name" : "Padama Reddy",
        "age":"35"
    },
    {
        "textbookname": "One Indian girl",
        "author name" : "Chetan Bhagath",
        "age":"35"
    },
    {
        "textbookname": "Scretly Yours",
        "author name" : "Unknown",
        "age":"51"
    },
    {
        "textbookname": "Three mistakes of life",
        "author name" : "Chetan Bhagath",
        "age":"35"
    },
    {
        "textbookname": "I too had a love story",
        "author name" : "Ravindra Singh",
        "age":"39"
    }
]

df=pd.DataFrame(data)
print(df)'''

import pandas as pd

books = {'Name': ['The Hobbit', 'Twilight', 'Jane Eyre', 'Animal Farm','The Kite Runner','Life of Pi','Eclipse','The Book Thief','The Giver','The Iliad'],
        'Author':['J. R. R. Tolkien','Stephenie Meyer','Charlotte Brontë','Animal Farm','Khaled Hosseini','Yann Martel','Stephenie Meyer','Markus Zusak ','Lois Lowry ',' Homer'],
         'Age':[78,67,68,67,37,76,45,67,78,37]}
df = pd.DataFrame(books)
print(df)


print(df.groupby('Age').size())

s=input("Enter the string")
print(df[df["textbookname"].str.contains(s)])