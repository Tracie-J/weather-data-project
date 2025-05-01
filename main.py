from weather_data import WeatherData

if __name__ == '__main__':
    # Create instance for Wilmington, NC event date 09/13/2025
    wilmington = WeatherData(34.225727, -77.944710, 9, 13, 2025)

    # Populate temperature attributes
    wilmington.five_year_avg_temp()
    wilmington.five_year_min_temp()
    wilmington.five_year_max_temp()

    # Populate wind speed attributes
    wilmington.five_year_avg_wind()
    wilmington.five_year_min_wind()
    wilmington.five_year_max_wind()

    # Populate precipitation attributes
    wilmington.five_year_precipitation_sum()
    wilmington.five_year_precipitation_min()
    wilmington.five_year_precipitation_max()


'''Test that I can populate and print accurate data from the weather_data file'''
    # print results
    print(wilmington.five_year_avg_temp())
    print(wilmington.five_year_min_temp())
    print(wilmington.five_year_max_temp())

    print(wilmington.five_year_avg_wind())
    print(wilmington.five_year_min_wind())
    print(wilmington.five_year_max_wind())

    print(wilmington.five_year_precipitation_sum())
    print(wilmington.five_year_precipitation_min())
    print(wilmington.five_year_precipitation_max())