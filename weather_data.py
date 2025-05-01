import requests
import json
from statistics import mean
import datetime


class WeatherData:
    '''This class holds historical weather data for a Wilmington, NC on Sept 13th. Section C1'''

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



    # method for mean temp in Fahrenheit. Section C2
    def five_year_avg_temp(self):
        #Determine where to start count back 5 years depending on if the event is today or in the future.
        today = datetime.date.today()
        evnt_date = datetime.date(self.year, self.month, self.day_of_month)

        if evnt_date > today:
            years = [self.year -i for i in range(5, 0, -1)]
        else:
            years = [self.year - i for i in range(4,-1,-1)]

        temperatures = []

        for year in years:
            date = f'{year}-{self.month:02d}-{self.day_of_month:02d}'
            url = 'https://archive-api.open-meteo.com/v1/archive'
            params = {
                'latitude': self.latitude,
                'longitude': self.longitude,
                'start_date': date,
                'end_date': date,
                'daily': ['temperature_2m_mean'],
                'timezone': 'America/New_York'  # timezone for Wilmington, NC
            }

            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                daily = data['daily']
                temperatures.append(daily['temperature_2m_mean'][0])
            else:
                print(f'Failed for {date}')

        # convert from celsius to farenheit
        for i, temp in enumerate(temperatures):
            temperatures[i] = temp * (9 / 5) + 32

        # Assign to attribute
        self.five_yr_avg_temp = round(mean(temperatures), 2)

        return self.five_yr_avg_temp



    # method for min temp in Fahrenheit. Section C2
    def five_year_min_temp(self):
        # Determine where to start count back 5 years depending on if the event is today or in the future.
        today = datetime.date.today()
        evnt_date = datetime.date(self.year, self.month, self.day_of_month)

        if evnt_date > today:
            years = [self.year - i for i in range(5, 0, -1)]
        else:
            years = [self.year - i for i in range(4, -1, -1)]

        temperatures = []

        for year in years:
            date = f'{year}-{self.month:02d}-{self.day_of_month:02d}'
            url = 'https://archive-api.open-meteo.com/v1/archive'
            params = {
                'latitude': self.latitude,
                'longitude': self.longitude,
                'start_date': date,
                'end_date': date,
                'daily': ['temperature_2m_mean'],
                'timezone': 'America/New_York'  # timezone for Wilmington, NC
            }

            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                daily = data['daily']
                temperatures.append(daily['temperature_2m_mean'][0])
            else:
                print(f'Failed for {date}')

        # convert from celsius to farenheit
        for i, temp in enumerate(temperatures):
            temperatures[i] = temp * (9 / 5) + 32

        # Assign to attribute
        self.five_yr_min_temp = round(min(temperatures), 2)

        return self.five_yr_min_temp



    # method for max temp in Fahrenheit. Section C2
    def five_year_max_temp(self):
        # Determine where to start count back 5 years depending on if the event is today or in the future.
        today = datetime.date.today()
        evnt_date = datetime.date(self.year, self.month, self.day_of_month)

        if evnt_date > today:
            years = [self.year - i for i in range(5, 0, -1)]
        else:
            years = [self.year - i for i in range(4, -1, -1)]

        temperatures = []

        for year in years:
            date = f'{year}-{self.month:02d}-{self.day_of_month:02d}'
            url = 'https://archive-api.open-meteo.com/v1/archive'
            params = {
                'latitude': self.latitude,
                'longitude': self.longitude,
                'start_date': date,
                'end_date': date,
                'daily': ['temperature_2m_mean'],
                'timezone': 'America/New_York'  # timezone for Wilmington, NC
            }

            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                daily = data['daily']
                temperatures.append(daily['temperature_2m_mean'][0])
            else:
                print(f'Failed for {date}')

        # convert from celsius to farenheit
        for i, temp in enumerate(temperatures):
            temperatures[i] = temp * (9 / 5) + 32

        # Assign to attribute
        self.five_yr_max_temp = round(max(temperatures), 2)

        return self.five_yr_max_temp




    # method for mean wind speed in miles per hour. Section C2
    def five_year_avg_wind(self):
        # Determine where to start count back 5 years depending on if the event is today or in the future.
        today = datetime.date.today()
        evnt_date = datetime.date(self.year, self.month, self.day_of_month)

        if evnt_date > today:
            years = [self.year - i for i in range(5, 0, -1)]
        else:
            years = [self.year - i for i in range(4, -1, -1)]

        wind_speed = []

        for year in years:
            date = f'{year}-{self.month:02d}-{self.day_of_month:02d}'
            url = 'https://archive-api.open-meteo.com/v1/archive'
            params = {
                'latitude': self.latitude,
                'longitude': self.longitude,
                'start_date': date,
                'end_date': date,
                'daily': ['wind_speed_10m_max'],
                'timezone': 'America/New_York'  # timezone for Wilmington, NC
            }

            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                daily = data['daily']
                wind_speed.append(daily['wind_speed_10m_max'][0])
            else:
                print(f'Failed for {date}')

        # convert from km/h to mph
        for i, wind in enumerate(wind_speed):
            wind_speed[i] = wind * 0.621371

        # Assign to attribute
        self.five_yr_avg_wind_speed = round(mean(wind_speed), 2)

        return self.five_yr_avg_wind_speed




    # write a method for min wind speed in miles per hour. Section C2
    def five_year_min_wind(self):
        # Determine where to start count back 5 years depending on if the event is today or in the future.
        today = datetime.date.today()
        evnt_date = datetime.date(self.year, self.month, self.day_of_month)

        if evnt_date > today:
            years = [self.year - i for i in range(5, 0, -1)]
        else:
            years = [self.year - i for i in range(4, -1, -1)]

        wind_speed = []

        for year in years:
            date = f'{year}-{self.month:02d}-{self.day_of_month:02d}'
            url = 'https://archive-api.open-meteo.com/v1/archive'
            params = {
                'latitude': self.latitude,
                'longitude': self.longitude,
                'start_date': date,
                'end_date': date,
                'daily': ['wind_speed_10m_max'],
                'timezone': 'America/New_York'  # timezone for Wilmington, NC
            }

            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                daily = data['daily']
                wind_speed.append(daily['wind_speed_10m_max'][0])
            else:
                print(f'Failed for {date}')

        # convert from km/h to mph
        for i, wind in enumerate(wind_speed):
            wind_speed[i] = wind * 0.621371

        # Assign to attribute
        self.five_yr_min_wind_speed = round(min(wind_speed), 2)

        return self.five_yr_min_wind_speed



    # write a method for maximum wind speed in miles per hour. Section C2
    def five_year_max_wind(self):
        # Determine where to start count back 5 years depending on if the event is today or in the future.
        today = datetime.date.today()
        evnt_date = datetime.date(self.year, self.month, self.day_of_month)

        if evnt_date > today:
            years = [self.year - i for i in range(5, 0, -1)]
        else:
            years = [self.year - i for i in range(4, -1, -1)]

        wind_speed = []

        for year in years:
            date = f'{year}-{self.month:02d}-{self.day_of_month:02d}'
            url = 'https://archive-api.open-meteo.com/v1/archive'
            params = {
                'latitude': self.latitude,
                'longitude': self.longitude,
                'start_date': date,
                'end_date': date,
                'daily': ['wind_speed_10m_max'],
                'timezone': 'America/New_York'  # timezone for Wilmington, NC
            }

            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                daily = data['daily']
                wind_speed.append(daily['wind_speed_10m_max'][0])
            else:
                print(f'Failed for {date}')

        # convert from km/h to mph
        for i, wind in enumerate(wind_speed):
            wind_speed[i] = wind * 0.621371

        # Assign to attribute
        self.five_yr_max_wind_speed = round(max(wind_speed), 2)

        return self.five_yr_max_wind_speed



    # method for precipitation sum in inches. Section C2
    def five_year_precipitation_sum(self):
        # Determine where to start count back 5 years depending on if the event is today or in the future.
        today = datetime.date.today()
        evnt_date = datetime.date(self.year, self.month, self.day_of_month)

        if evnt_date > today:
            years = [self.year - i for i in range(5, 0, -1)]
        else:
            years = [self.year - i for i in range(4, -1, -1)]

        precipitation = []

        for year in years:
            date = f'{year}-{self.month:02d}-{self.day_of_month:02d}'
            url = 'https://archive-api.open-meteo.com/v1/archive'
            params = {
                'latitude': self.latitude,
                'longitude': self.longitude,
                'start_date': date,
                'end_date': date,
                'daily': ['precipitation_sum'],
                'timezone': 'America/New_York'  # timezone for Wilmington, NC
            }

            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                daily = data['daily']
                precipitation.append(daily['precipitation_sum'][0])
            else:
                print(f'Failed for {date}')

        # convert form millimeters (mm) to inches
        for i, p in enumerate(precipitation):
            precipitation[i] = p / 25.4

        # Assign to attribute
        self.five_yr_sum_precipitation = round(sum(precipitation), 2)

        return self.five_yr_sum_precipitation



# method for precipitation min in inches. Section C2
    def five_year_precipitation_min(self):
        # Determine where to start count back 5 years depending on if the event is today or in the future.
        today = datetime.date.today()
        evnt_date = datetime.date(self.year, self.month, self.day_of_month)

        if evnt_date > today:
            years = [self.year - i for i in range(5, 0, -1)]
        else:
            years = [self.year - i for i in range(4, -1, -1)]

        precipitation = []

        for year in years:
            date = f'{year}-{self.month:02d}-{self.day_of_month:02d}'
            url = 'https://archive-api.open-meteo.com/v1/archive'
            params = {
                'latitude': self.latitude,
                'longitude': self.longitude,
                'start_date': date,
                'end_date': date,
                'daily': ['precipitation_sum'],
                'timezone': 'America/New_York'  # timezone for Wilmington, NC
            }

            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                daily = data['daily']
                precipitation.append(daily['precipitation_sum'][0])
            else:
                print(f'Failed for {date}')

        # convert form millimeters (mm) to inches
        for i, p in enumerate(precipitation):
            precipitation[i] = p / 25.4

        # Assign to attribute
        self.five_yr_min_precipitation = round(min(precipitation), 2)

        return self.five_yr_min_precipitation


# method for precipitation max in inches. Section C2
    def five_year_precipitation_max(self):
        # Determine where to start count back 5 years depending on if the event is today or in the future.
        today = datetime.date.today()
        evnt_date = datetime.date(self.year, self.month, self.day_of_month)

        if evnt_date > today:
            years = [self.year - i for i in range(5, 0, -1)]
        else:
            years = [self.year - i for i in range(4, -1, -1)]

        precipitation = []

        for year in years:
            date = f'{year}-{self.month:02d}-{self.day_of_month:02d}'
            url = 'https://archive-api.open-meteo.com/v1/archive'
            params = {
                'latitude': self.latitude,
                'longitude': self.longitude,
                'start_date': date,
                'end_date': date,
                'daily': ['precipitation_sum'],
                'timezone': 'America/New_York'  # timezone for Wilmington, NC
            }

            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                daily = data['daily']
                precipitation.append(daily['precipitation_sum'][0])
            else:
                print(f'Failed for {date}')

        # convert form millimeters (mm) to inches
        for i, p in enumerate(precipitation):
            precipitation[i] = p / 25.4

        # Assign to attribute
        self.five_yr_max_precipitation = round(max(precipitation), 2)

        return self.five_yr_max_precipitation







# Fetch data from the open meteo weather api to test if it's working properly
'''def fetch_weather_data(latitude, longitude, date):
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

# Location and date information for Wilmington, NC
# latitude = 34.225727
# longitude = -77.944710

# test that the connection to the api is working
# weather_data = fetch_weather_data(latitude, longitude, date)
# print(weather_data)
'''
# test temperature method
    # avg_temp = five_year_avg_temp(latitude, longitude, month, day)
    # print(avg_temp)

# test wind speed method
    # max_wind_speed = five_year_max_wind(latitude, longitude, month, day)
    # print(max_wind_speed)

# test precipitation method
    # precip_sum = five_year_precipitation_sum(latitude, longitude, month, day)
    # print(precip_sum)

'''test results
Before conversions:
{'avg_temp': 24.38, 'min_temp': 23.0, 'max_temp': 25.9, 'avg_wind': 18.32, 'min_wind': 9.8, 'max_wind': 30.2, 
'sum_precip': 99.5, 'min_precip': 0.0, 'max_precip': 92.2}

After conversions:
{'avg_temp': 75.88, 'min_temp': 73.4, 'max_temp': 78.62, 'avg_wind': 11.38, 'min_wind': 6.09, 'max_wind': 18.77, 
'sum_precip': 3.92, 'min_precip': 0.0, 'max_precip': 3.63}
'''