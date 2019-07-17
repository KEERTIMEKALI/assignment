from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def index2():
    return render_template('index2.html')

@app.route('/flaskex2')
def index3():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=8000)
