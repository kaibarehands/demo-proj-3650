import requests

def get_weather(latitude: float, longitude: float, api_key: str) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,uv_index,precipitation"
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    data = response.json()

    return {
        "temperature": data["current"]["temperature_2m"],
        "uv_index": data["current"]["uv_index"],
        "precipitation": data["current"]["precipitation"],
        "unit": data["current_units"]["temperature_2m"],
        "uv_index_unit": data["current_units"]["uv_index"],
        "precipitation_unit": data["current_units"]["precipitation"],
        "latitude": latitude,
        "longitude": longitude
    }