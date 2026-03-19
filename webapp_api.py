from flask import Flask, request, jsonify
import weather

app = Flask(__name__)

# GET endpoint for weather/temperature
@app.route('/get-temp', methods=['GET'])
def get_temperature():
    try:
        latitude = request.args.get('latitude', type=float)
        longitude = request.args.get('longitude', type=float)
        api_key = request.args.get('api_key', default='', type=str)
        
        if latitude is None or longitude is None:
            return jsonify({"error": "latitude and longitude are required"}), 400
        
        result = weather.get_temp(latitude, longitude, api_key)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# GET endpoint for precipitation
@app.route('/get-precip', methods=['GET'])
def get_precipitation():
    try:
        latitude = request.args.get('latitude', type=float)
        longitude = request.args.get('longitude', type=float)
        api_key = request.args.get('api_key', default='', type=str)
        
        if latitude is None or longitude is None:
            return jsonify({"error": "latitude and longitude are required"}), 400
        
        result = weather.get_precip(latitude, longitude, api_key)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# GET endpoint for UV index
@app.route('/get-uv', methods=['GET'])
def get_uv_index():
    try:
        latitude = request.args.get('latitude', type=float)
        longitude = request.args.get('longitude', type=float)
        api_key = request.args.get('api_key', default='', type=str)
        
        if latitude is None or longitude is None:
            return jsonify({"error": "latitude and longitude are required"}), 400
        
        result = weather.get_uv(latitude, longitude, api_key)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)


