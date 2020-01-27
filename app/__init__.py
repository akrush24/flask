#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def root():
    return "[HOME]"

@app.route("/hello")
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>', methods=['GET','POST'])
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    pass

if __name__ == "__main__":
    app.run()
