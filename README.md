# Weather Prediction Project

## Description
This project uses an API to retrieve weather data at a set day and time. The data is then processed to create aggregate 
results. All records are stored in a SQLite database. SQLAlchemy is used for database interactions.

## Requirements
Python 3.12

Dependencies:
* requests - retrieves weather data from the API
* SQLAlchemy - interacts with the SQLite database

Install Dependencies:
Dependencies can be installed by using the Python Interpreter under Settings or pip install -r requirements.txt in the 
terminal.

## Inputs
You will need to choose a location and date.
* Latitude - The latitude of your chosen city.
* Longitude - The longitude of your chosen city.
* Month - Integer representing your chosen month.
* Day of Month - Integer representing your chosen day of the month.
* Year - Integer representing your chosen year.

## Outputs
When main.py is run:
1. Weather Data Retrieval:
* Average Temperature in Fahrenheit
* Minimum Temperature in Fahrenheit
* Maximum Temperature in Fahrenheit
* Average Wind Speed in MPH
* Minimum Wind Speed in MPH
* Maximum Wind Speed in MPH
* Total Precipitation in Inches
* Minimum Precipitation in Inches
* Maximum Precipitation in Inches

Example Output after conversion: {'avg_temp': 75.88, 'min_temp': 73.4, 'max_temp': 78.62, 'avg_wind': 11.38, 'min_wind': 6.09, 'max_wind': 18.77, 
'sum_precip': 3.92, 'min_precip': 0.0, 'max_precip': 3.63}

2. SQLite Database insert
* The weather data is inserted from the retrieval process into weather.db under the
weather_records table.

3. Database Query
* The display weather data function will query the database and print the formatted weather data.

4. UnitTest
* test.py can be run to test if the temperature conversion and range is working properly and reasonable,
the precipitation sum is positive and reasonable, and the database insert works. If all is working 
output will be 'Ran 3 tests in ####s   Ok'

## Commands
1. Run the weather_data.py file first to initialize the classes that will be used later
to retrieve data from the api, create the database, and retrieve records from the database.
2. In the main.py file insert your latitude, longitude, month, day_of_month, and year into
the location variable (located near the top of the file).
3. Run the main.py file. This will use the WeatherData class to call the API and retrieve
the information. The WeatherTable class will create a table in SQLite and the file will store
the records in the table and query it.

## Sources
* This project uses historical weather data collected from the [Open-Meteo API](https://archive-api.open-meteo.com/v1/archive).
This API provides access to daily weather data such as temperature, wind speed, and precipitation
for specific coordinates and dates.