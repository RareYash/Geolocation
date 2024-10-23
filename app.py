from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import joblib
import pandas as pd
import numpy as np

model_file = "kmeans_model.pkl"
kmeans_loaded = joblib.load(model_file)

cluster_mapping = {
    0: 'Low-budget, far from universities, near restaurants',
    1: 'Medium-budget, moderate distance from universities, basic amenities',
    2: 'High-budget, close to universities, premium amenities'
}


def predict_cluster(input_data):
    df_from_json = pd.DataFrame.from_dict([input_data])
    return cluster_mapping[np.squeeze(kmeans_loaded.predict(df_from_json)).item()]


app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


def preprocess_input(input_data):
    output_data = {
        "flat_price": 0,
        "fav_food": 0,
        "eating_out": 0,
        "income": 0,
        "location_Agripada": 1,
        "location_Andheri": 0,
        "location_Bandra": 0,
        "location_Bhandup": 0,
        "location_Bhayandar": 0,
        "location_Boisar": 0,
        "location_Borivali": 0,
        "location_Byculla": 0,
        "location_Chembur": 0,
        "location_Churchgate": 0,
        "location_Colaba": 0,
        "location_Cuffe": 0,
        "location_Cumballa": 0,
        "location_Dadar": 0,
        "location_Dahisar": 0,
        "location_Ghatkopar": 0,
        "location_Girgaon": 0,
        "location_Goregaon": 0,
        "location_Govandi": 0,
        "location_Jogeshwari": 0,
        "location_Kamathipura": 0,
        "location_Kandivali": 0,
        "location_Kanjurmarg": 0,
        "location_Khar": 0,
        "location_Kurla": 0,
        "location_Lower": 0,
        "location_Madanpura": 0,
        "location_Madh": 0,
        "location_Mahalakshmi": 0,
        "location_Mahim": 0,
        "location_Malabar": 0,
        "location_Malad": 0,
        "location_Marine": 0,
        "location_Matunga": 0,
        "location_Mazgaon": 0,
        "location_Mira Road": 0,
        "location_Mulund": 0,
        "location_Mumbai": 0,
        "location_Naigaon": 0,
        "location_Nalasopara": 0,
        "location_Palghar": 0,
        "location_Parel": 0,
        "location_Powai": 0,
        "location_Prabhadevi": 0,
        "location_Sakinaka": 0,
        "location_Santacruz": 0,
        "location_Sewri": 0,
        "location_Sion": 0,
        "location_Tardeo": 0,
        "location_Thane": 0,
        "location_Vasai": 0,
        "location_Vikhroli": 0,
        "location_Vile Parle": 0,
        "location_Virar": 0,
        "location_Wadala": 0,
        "location_Worli": 0,
        "location_others": 0
    }
    
    output_data['flat_price'] = float(input_data['flat_price'])
    output_data['fav_food'] = int(input_data['fav_food'])
    output_data['eating_out'] = int(input_data['eating_out'])
    output_data['income'] = int(input_data['income'])

    output_data[input_data['location']] = 1
    return output_data


@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.get_json()
    input_data = preprocess_input(input_data)
    if input_data is None:
        return jsonify({"error": "Invalid input"}), 400

    try:
        prediction = predict_cluster(input_data)
        return jsonify({"prediction": prediction}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
