from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load the models and the scaler
try:
    reg_model = joblib.load('regression_model.pkl')
    clf_model = joblib.load('classification_model.pkl')
    scaler = joblib.load('scaler.pkl')
    label_encoder = joblib.load('label_encoder.pkl')
    logger.info("Models loaded successfully")
except Exception as e:
    logger.error("Error loading models: %s", e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_weight', methods=['POST'])
def predict_weight():
    try:
        data = request.json
        features = np.array([[data['length1'], data['length2'], data['length3'], data['height'], data['width']]])
        scaled_features = scaler.transform(features)
        weight = reg_model.predict(scaled_features)
        return jsonify({'weight': weight[0]})
    except Exception as e:
        logger.error("Error in predict_weight: %s", e)
        return jsonify({'error': str(e)})

@app.route('/predict_species', methods=['POST'])
def predict_species():
    try:
        data = request.json
        features = np.array([[data['length1'], data['length2'], data['length3'], data['height'], data['width']]])
        scaled_features = scaler.transform(features)
        species_index = clf_model.predict(scaled_features)
        species = label_encoder.inverse_transform(species_index)
        return jsonify({'species': species[0]})
    except Exception as e:
        logger.error("Error in predict_species: %s", e)
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
