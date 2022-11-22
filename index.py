from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import numpy as np
import cv2
import urllib.request

app = Flask(__name__)
cors = CORS(app)

# -------------------------
IMG_DIMN = 224
CALORIES_MAX = 9485.81543
MASS_MAX = 7975
FAT_MAX = 875.5410156
CARB_MAX = 844.5686035
PROTEIN_MAX = 147.491821
# -------------------------

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

def preprocess_image(img_path):
    req = urllib.request.urlopen(img_path)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (IMG_DIMN, IMG_DIMN))
    img = (img / 255.0)
    return img


""" def load_model():
    model = keras.models.load_model('modelo_nutrition5k_inception.h5')
    model.compile(optimizer=Adam(lr=1e-5), loss='MSE')
    return model """


def denormalize_outputs(outputs):
    cal = outputs[0] * CALORIES_MAX
    mass = outputs[1] * MASS_MAX
    fat = outputs[2] * FAT_MAX
    carb = outputs[3] * CARB_MAX
    prot = outputs[4] * PROTEIN_MAX
    return {'cal:': str(cal),
            'mass': str(mass),
            'fat': str(fat),
            'carb': str(carb),
            'prot': str(prot)}