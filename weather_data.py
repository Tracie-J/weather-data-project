import requests
from statistics import mean
import datetime
from sqlalchemy import Column, Float, Integer
from sqlalchemy.orm import declarative_base


# This class holds historical weather data for a Wilmington, NC on Sept 13th. Section C1
class WeatherData:
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



    # method for calculating five year attributes data. Section C2
    def five_year_data(self):

        #Determine where to start count back 5 years depending on if the event is today or in the future.
        today = datetime.date.today()
        evnt_date = datetime.date(self.year, self.month, self.day_of_month)

        if evnt_date > today:
            years = [self.year -i for i in range(5, 0, -1)]
        else:
            years = [self.year - i for i in range(4,-1,-1)]

        # create lists to hold the temp, wind, and precipitation data
        temperatures = []
        wind_speed = []
        precipitation = []

        for year in years:
            date = f'{year}-{self.month:02d}-{self.day_of_month:02d}'
            url = 'https://archive-api.open-meteo.com/v1/archive'
            params = {
                'latitude': self.latitude,
                'longitude': self.longitude,
                'start_date': date,
                'end_date': date,
                'daily': ['temperature_2m_mean', 'wind_speed_10m_max', 'precipitation_sum'],
                'timezone': 'America/New_York'  # timezone for Wilmington, NC
            }

            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                daily = data['daily']
                temperatures.append(daily['temperature_2m_mean'][0])
                wind_speed.append(daily['wind_speed_10m_max'][0])
                precipitation.append(daily['precipitation_sum'][0])
            else:
                print(f'Failed for {date}')

        # convert temperature from celsius to fahrenheit
        for i, temp in enumerate(temperatures):
            temperatures[i] = temp * (9 / 5) + 32

        # convert wind speed from km/h to mph
        for i, wind in enumerate(wind_speed):
            wind_speed[i] = wind * 0.621371

        # convert precipitation form millimeters (mm) to inches
        for i, p in enumerate(precipitation):
            precipitation[i] = p / 25.4

        # Assign to attributes
        self.five_yr_avg_temp = round(mean(temperatures), 2)
        self.five_yr_min_temp = round(min(temperatures), 2)
        self.five_yr_max_temp = round(max(temperatures), 2)

        self.five_yr_avg_wind_speed = round(mean(wind_speed), 2)
        self.five_yr_min_wind_speed = round(min(wind_speed), 2)
        self.five_yr_max_wind_speed = round(max(wind_speed), 2)

        self.five_yr_sum_precipitation = round(sum(precipitation), 2)
        self.five_yr_min_precipitation = round(min(precipitation), 2)
        self.five_yr_max_precipitation = round(max(precipitation), 2)


        return (self.five_yr_avg_temp, self.five_yr_min_temp, self.five_yr_max_temp, self.five_yr_avg_wind_speed,
                self.five_yr_min_wind_speed, self.five_yr_max_wind_speed, self.five_yr_sum_precipitation,
                self.five_yr_min_precipitation, self.five_yr_max_precipitation)


# Create a class that creates a table in SQLite using SQLAlchemy ORM. Section C4
Base = declarative_base()

class WeatherTable(Base):
    '''This class creates a table using SQLAlchemy ORM. Section C4'''
    __tablename__ = 'weather_records'

    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    month = Column(Integer)
    day_of_month = Column(Integer)
    year = Column(Integer)
    five_yr_average_temp = Column(Float)
    five_yr_min_temp = Column(Float)
    five_yr_max_temp = Column(Float)
    five_yr_avg_wind_speed = Column(Float)
    five_yr_min_wind_speed = Column(Float)
    five_yr_max_wind_speed = Column(Float)
    five_yr_sum_precipitation = Column(Float)
    five_yr_min_precipitation = Column(Float)
    five_yr_max_precipitation = Column(Float)







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