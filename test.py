import unittest
from weather_data import WeatherData, Base, WeatherTable
from sqlalchemy import  create_engine
from sqlalchemy.orm import  sessionmaker

#create test cases. Section D.
class TestWeatherData(unittest.TestCase):

    # create sqlite database in memory to test cases.
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        # Sample weather data
        self.weather = WeatherData(34.225727, -77.944710, 9, 13, 2025)
        self.weather.five_year_data()

    def test_temp_conversion(self):
        # test if the Fahrenheit conversion is in a normal range
        self.assertGreater(self.weather.five_yr_avg_temp, -90) # lowest temp in the US recorded at -80
        self.assertLess(self.weather.five_yr_avg_temp, 140) # highest temp in the US recorded at 134

    def test_precipitation_sum(self):
        # tests if the precipitation is not negative and overall reasonable
        self.assertGreater(self.weather.five_yr_sum_precipitation, 0) # cannot have negative precipitation
        self.assertLess(self.weather.five_yr_sum_precipitation, 52) # record for max U.S. rainfall within 24hrs is 49.69

    def test_database_insert(self):
        # Test insert and retrieve record from table
        record = WeatherTable(
            latitude=self.weather.latitude,
            longitude=self.weather.longitude,
            month=self.weather.month,
            day_of_month=self.weather.day_of_month,
            year=self.weather.year,
            five_yr_average_temp=self.weather.five_yr_avg_temp,
            five_yr_min_temp=self.weather.five_yr_min_temp,
            five_yr_max_temp=self.weather.five_yr_max_temp,
            five_yr_avg_wind_speed=self.weather.five_yr_avg_wind_speed,
            five_yr_min_wind_speed=self.weather.five_yr_min_wind_speed,
            five_yr_max_wind_speed=self.weather.five_yr_max_wind_speed,
            five_yr_sum_precipitation=self.weather.five_yr_sum_precipitation,
            five_yr_min_precipitation=self.weather.five_yr_min_precipitation,
            five_yr_max_precipitation=self.weather.five_yr_max_precipitation
        )
        self.session.add(record)
        self.session.commit()

        result = self.session.query(WeatherTable).filter_by(latitude=34.225727).first()
        self.assertIsNotNone(result)
        self.assertEqual(result.month, 9)


if __name__ == '__main__':
    unittest.main()
