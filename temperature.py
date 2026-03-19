import requests

def get_temperature(latitude: float, longitude: float, api_key: str) -> dict:
    """
    Fetch temperature data for a given location using Open-Meteo API (free, no key required).
    
    Args:
        latitude: Location latitude
        longitude: Location longitude
        api_key: Not needed for Open-Meteo, but kept for compatibility
        
    Returns:
        dict with temperature data
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code"
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    data = response.json()
    return {
        "temperature": data["current"]["temperature_2m"],
        "unit": data["current_units"]["temperature_2m"],
        "latitude": latitude,
        "longitude": longitude
    }