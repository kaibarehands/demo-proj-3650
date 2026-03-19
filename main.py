from weather import get_precip, get_temp, get_uv

# 39.3292° N, 82.1013° W - Athens,  OH
def main():
    latitude = 39.3292
    longitude = -82.1013
    temp_data = get_temp(latitude, longitude, "")
    uv_data = get_uv(latitude, longitude, "")
    precip_data = get_precip(latitude, longitude, "")


    
if __name__ == "__main__":
    main()