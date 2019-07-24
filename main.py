from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')# it is used to copen the browser
def fun():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
    val = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    email = request.form.get('email')
    passwd = request.form.get('passwd')

    if email == 'kkk@example.com' and passwd == '345':
        return render_template('s1.html', val=val)
    elif email == 'kkk@example.com':
        return "<h1>Password is wrong </h1>"
    elif passwd == '343':
        return "<h1>Email is wrong </h1>"
    else:
        return "<h1> Invalid email or password...</h1>"

@app.route('/num', methods=['GET','POST'])
def number():
    sel_num=request.form.get('mylist',type=int)
    return render_template('s2.html', val=sel_num)


if __name__ == "__main__":
    app.run()
