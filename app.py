from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the models and the scaler
reg_model = joblib.load('regression_model.pkl')
clf_model = joblib.load('classification_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_weight', methods=['POST'])
def predict_weight():
    data = request.json
    features = np.array([[data['length1'], data['length2'], data['length3'], data['height'], data['width']]])
    scaled_features = scaler.transform(features)
    weight = reg_model.predict(scaled_features)
    return jsonify({'weight': weight[0]})

@app.route('/predict_species', methods=['POST'])
def predict_species():
    data = request.json
    features = np.array([[data['length1'], data['length2'], data['length3'], data['height'], data['width']]])
    scaled_features = scaler.transform(features)
    species_index = clf_model.predict(scaled_features)
    species = label_encoder.inverse_transform(species_index)
    return jsonify({'species': species[0]})

if __name__ == '__main__':
    app.run(debug=True)
