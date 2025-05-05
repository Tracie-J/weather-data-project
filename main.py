from weather_data import WeatherData

if __name__ == '__main__':
    # Create instance for Wilmington, NC event date 09/13/2025
    wilmington = WeatherData(34.225727, -77.944710, 9, 13, 2025)

    # Populate temperature, wind speed, and precipitation attributes
    wilmington.five_year_data()



'''Test that I can populate and print accurate data from the weather_data file'''
# print results
print(wilmington.five_year_data())

'''test results
Before conversions:
{'avg_temp': 24.38, 'min_temp': 23.0, 'max_temp': 25.9, 'avg_wind': 18.32, 'min_wind': 9.8, 'max_wind': 30.2, 
'sum_precip': 99.5, 'min_precip': 0.0, 'max_precip': 92.2}

After conversions:
{'avg_temp': 75.88, 'min_temp': 73.4, 'max_temp': 78.62, 'avg_wind': 11.38, 'min_wind': 6.09, 'max_wind': 18.77, 
'sum_precip': 3.92, 'min_precip': 0.0, 'max_precip': 3.63}
'''