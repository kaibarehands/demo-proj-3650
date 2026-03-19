from weather import get_weather

# 39.3292° N, 82.1013° W
def main():
    latitude = 39.3292
    longitude = -82.1013
    weather_data = get_weather(latitude, longitude, "")

    
if __name__ == "__main__":
    main()