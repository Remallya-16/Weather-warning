import sys

def weather_warning(city, condition, temperature, rainfall, wind_speed):
    condition = condition.lower()

    if temperature >= 40:
        return f"{city}: Heatwave Warning"
    elif rainfall >= 100:
        return f"{city}: Heavy Rain Warning"
    elif wind_speed >= 60:
        return f"{city}: Storm Warning"
    elif condition == "fog":
        return f"{city}: Fog Alert"
    else:
        return f"{city}: Normal Weather"


if __name__ == "__main__":
    
    if len(sys.argv) == 6:
        city = sys.argv[1]
        condition = sys.argv[2]
        temperature = int(sys.argv[3])
        rainfall = int(sys.argv[4])
        wind_speed = int(sys.argv[5])

    else:
        city = input("Enter city: ")
        condition = input("Enter condition: ")
        temperature = int(input("Enter temperature: "))
        rainfall = int(input("Enter rainfall: "))
        wind_speed = int(input("Enter wind speed: "))

    print(weather_warning(city, condition, temperature, rainfall, wind_speed))

