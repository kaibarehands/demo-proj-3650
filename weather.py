import requests


def _get_current_data(latitude: float, longitude: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,uv_index,precipitation"
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_temp(latitude: float, longitude: float, api_key: str) -> dict:
    data = _get_current_data(latitude, longitude)

    return {
        "temperature": data["current"]["temperature_2m"],
        "unit": data["current_units"]["temperature_2m"],
        "latitude": latitude,
        "longitude": longitude
    }


def get_uv(latitude: float, longitude: float, api_key: str) -> dict:
    data = _get_current_data(latitude, longitude)

    return {
        "uv_index": data["current"]["uv_index"],
        "uv_index_unit": data["current_units"]["uv_index"],
        "latitude": latitude,
        "longitude": longitude
    }


def get_precip(latitude: float, longitude: float, api_key: str) -> dict:
    data = _get_current_data(latitude, longitude)

    return {
        "precipitation": data["current"]["precipitation"],
        "precipitation_unit": data["current_units"]["precipitation"],
        "latitude": latitude,
        "longitude": longitude
    }