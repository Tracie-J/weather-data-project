import requests
import json

class WeatherData:
    '''This class holds historical weather data for a Wilmington, NC on Sept 13th.'''

    def __init__(self, latitude, longitude, month, day_of_month, year):
        '''
        Initialize WeatherData with the location and date information. The weather attributes will
        be added later. latitude (float), longitude (float), month (int), day_of_month (int),
        year (int)
        '''
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day_of_month = day_of_month
        self.year = year
        self.five_yr_avg_temp = None
        self.five_yr_min_temp = None
        self.five_yr_max_temp = None
        self.five_yr_avg_wind_speed = None
        self.five_yr_min_wind_speed = None
        self.five_yr_max_wind_speed = None
        self.five_yr_sum_precipitation = None
        self.five_yr_min_precipitation = None
        self.five_yr_max_precipitation = None


# write a method for mean temp in Fahrenheit, max wind speed in miles per hour, and precipitation sum in inches.
def fetch_weather_data(latitude, longitude, date):
    url = 'https://archive-api.open-meteo.com/v1/archive'

    params = {
        'latitude': latitude,
        'longitude': longitude,
        'start_date': date,
        'end_date': date,
        'daily': ['temperature_2m_mean', 'wind_speed_10m_max', 'precipitation_sum'],
        'timezone': 'America/New_York' #timezone for Wilmington, NC
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Failed to fetch data: {response.status_code}')
        return None

latitude = 34.225727
longitude = -77.944710
date = '2024-09-13'

weather_data = fetch_weather_data(latitude, longitude, date)
print(weather_data)


# write a method for maximum wind speed in miles per hour

# write a method for precipitation sum in inches