from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "index!"

if __name__ == "__main__":
    app.run()

@app.route('/hello')
def hello():
    return 'Hello World'
