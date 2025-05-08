from requests import Session
from weather_data import WeatherData, WeatherTable, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an instance of the class and call the methods in part C2. Section C3
if __name__ == '__main__':
    # Create instance for Wilmington, NC event date 09/13/2025
    wilmington = WeatherData(34.225727, -77.944710, 9, 13, 2025)

    # Populate temperature, wind speed, and precipitation attributes
    wilmington.five_year_data()


'''Section C5.'''
# Set up SQLite engine and session. Section C5
engine = create_engine('sqlite:///weather.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Populate WeatherTable with data from WeatherData
record = WeatherTable(
    latitude=wilmington.latitude,
    longitude=wilmington.longitude,
    month=wilmington.month,
    day_of_month=wilmington.day_of_month,
    year=wilmington.year,
    five_yr_average_temp=wilmington.five_yr_avg_temp,
    five_yr_min_temp =wilmington.five_yr_min_temp,
    five_yr_max_temp =wilmington.five_yr_max_temp,
    five_yr_avg_wind_speed =wilmington.five_yr_avg_wind_speed,
    five_yr_min_wind_speed =wilmington.five_yr_min_wind_speed,
    five_yr_max_wind_speed =wilmington.five_yr_max_wind_speed,
    five_yr_sum_precipitation =wilmington.five_yr_sum_precipitation,
    five_yr_min_precipitation =wilmington.five_yr_min_precipitation,
    five_yr_max_precipitation =wilmington.five_yr_max_precipitation
)

# Add and commit to the database.
if not exists:
    session.add(record)
    session.commit()
    # Checks that everything is successful
    print('Add successfully to the database')
else:
    print('Data already added')

# Create method that queries the data stored in the database from C5. Section C6
for record in session.query(WeatherTable).all():
    print(vars(record))



'''Test that I can populate and print accurate data from the weather_data file'''
# print results
# print(wilmington.five_year_data())

'''test results
Before conversions:
{'avg_temp': 24.38, 'min_temp': 23.0, 'max_temp': 25.9, 'avg_wind': 18.32, 'min_wind': 9.8, 'max_wind': 30.2, 
'sum_precip': 99.5, 'min_precip': 0.0, 'max_precip': 92.2}

After conversions:
{'avg_temp': 75.88, 'min_temp': 73.4, 'max_temp': 78.62, 'avg_wind': 11.38, 'min_wind': 6.09, 'max_wind': 18.77, 
'sum_precip': 3.92, 'min_precip': 0.0, 'max_precip': 3.63}
'''