class WeatherData:
    '''This class holds historical weather data for a set location and date.'''

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
        self. five_yr_min_wind_speed = None
        self.five_yr_max_wind_speed = None
        self.five_yr_sum_precipiation = None
        self.five_yr_min_precipiation = None
        self.five_yr_max_precipiation = None