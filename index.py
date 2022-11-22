from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!sadgfhghdfgh</p>"

@app.route('/about')
def about():
    return 'About Page Route'

@cross_origin
@app.route('/prueba', methods=['POST'])
def prueba():
    ruta = request.json
    return jsonify(ruta)