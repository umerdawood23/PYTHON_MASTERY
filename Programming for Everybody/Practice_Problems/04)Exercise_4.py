weather_data = {
    "region": "North America",
    "stations": [
        {
            "city": "New York",
            "metrics": {"temp_c": 22.5, "humidity": 60, "wind_kmh": 15}
        },
        {
            "city": "Chicago",
            "metrics": {"temp_c": 18.0, "humidity": 75, "wind_kmh": 25}
        },
        {
            "city": "Denver",
            "metrics": {"temp_c": 15.5, "humidity": 40, "wind_kmh": 20}
        }
    ]
}

total_temp = 0.0
highest_wind = 0.0
windy_city = ""
station_count = len(weather_data["stations"])

# Loop through each station inside the list
for station in weather_data["stations"]:
    city_name = station["city"]
    temp = station["metrics"]["temp_c"]
    wind = station["metrics"]["wind_kmh"]
    
    print(f"City: {city_name} | Temperature: {temp}°C")
    
    # Add to total temperature for the average
    total_temp = total_temp + temp
    
    # Check for the highest wind speed
    if wind > highest_wind:
        highest_wind = wind
        windy_city = city_name

# Calculate average temperature
average_temperature = total_temp / station_count

print("-" * 30)
print(f"Average Temperature: {average_temperature}°C")
print(f"Highest Wind Speed: {windy_city} ({highest_wind} km/h)")