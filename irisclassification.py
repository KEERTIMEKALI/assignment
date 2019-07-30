from PIL import Image
import csv
from flask import Flask, render_template, request
import pandas as pd

df = pd.read_csv('iris.data', header = 0)
'''df = df.reset_index()'''

n=len(df)
'''df.head()'''
app = Flask(__name__)

@app.route('/')
def index3():
    return render_template('irisclassificationex.html')

@app.route('/submit',methods=['GET','POST'])
def index2():
    spl = request.form.get('sepal_length',type=float)
    spw = request.form.get('sepal_width',type=float)
    pel = request.form.get('petal_length',type=float)
    pew = request.form.get('petal_width',type=float)

    print(spl,spw,pel,pew)
    if spl<4.3 or spl>7.9:
        return "the value for sepal length is invalid"
    if spw<2.0 or spw>4.4:
        return "the value for sepal width is invalid"
    if pel<1.0 or pel>6.9:
        return "the value for petal length is invalid"
    if pew<0.1 or pew>2.5:
        return "the value for petal width is invalid"
    if (spl > 4.3 and spl < 5.8) and (spw>2.3 and spw<4.4) and (pel > 1.0 and pel < 1.9) and (pew > 0.1 and pew < 0.6):
        return "The species is SETOSA"
        myImage=Image.open('irissetosa.jpg')
        myImage.show();
    elif (spl > 4.9 and spl < 7.0) and (spw > 2.0 and spw < 3.4) and (pel > 3.0 and pel < 5.1) and (pew > 1.0 and pew < 1.8):
        return "The species is VERSICOLOR"
    elif (spl > 4.9 and spl < 7.9) and (spw > 2.2 and spw < 3.8) and (pel > 4.5 and pel < 6.9) and (pew > 1.4 and pew < 2.5):
        return "The species is VERGINICA"
    else:
        return "Does not belong to any SPECIES"

if __name__ == "__main__":
    app.run()