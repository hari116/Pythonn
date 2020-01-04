from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)  # app = flask.Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to flask'


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')


@app.route('/hello/<name>/<int:age>')
def hello(name, age):
    return 'hello %s of age %d' % (name, age)


# app.add_url_rule('/', 'hello', hello)

if __name__ == '__main__':
    app.run(debug=True)
