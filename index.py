from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!sadgfhghdfgh</p>"

@app.route('/about')
def about():
    return 'About Page Route'