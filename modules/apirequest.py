"""

"""
class APIManager:

    def __init__(self):
        #modules as attributes of a class (this is one way to avoid having to make the imports on the main code)
        self.openmeteo_requests =  __import__('openmeteo_requests')
        self.requests_cache =  __import__('requests_cache')
        self.pandas =  __import__('pandas')
        self.retry_requests =  __import__('retry_requests')

    def api_request_connection(self, longitude_:str, latitude_:str)->None:
        """
        Method
        """
        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = self.requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = self.retry_requests.retry(cache_session, retries = 5, backoff_factor = 0.2)
        self.openmeteo = self.openmeteo_requests.Client(session = retry_session)

        # Make sure all required weather variables are listed here
        # The order of variables in hourly or daily is important to assign them correctly below
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude_,
            "longitude": longitude_,
            "hourly": "temperature_2m"
        }
        self.responses = self.openmeteo.weather_api(url, params=params)
        self.print_request(self.responses[0])

    def print_request(self, data)->None:
        """
        Method
        """
        # Process first location. Add a for-loop for multiple locations or weather models
        print(f"Coordinates {data.Latitude()}°N {data.Longitude()}°E")
        print(f"Elevation {data.Elevation()} m asl")
        print(f"Timezone {data.Timezone()} {data.TimezoneAbbreviation()}")
        print(f"Timezone difference to GMT+0 {data.UtcOffsetSeconds()} s")

        # Process hourly data. The order of variables needs to be the same as requested.
        hourly = data.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

        hourly_data = {"date": self.pandas.date_range(
            start = self.pandas.to_datetime(hourly.Time(), unit = "s", utc = True),
            end = self.pandas.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
            freq = self.pandas.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
        )}
        hourly_data["temperature_2m"] = hourly_temperature_2m

        hourly_dataframe = self.pandas.DataFrame(data = hourly_data)
        print(hourly_dataframe)
        print("That would be an example over what you could do with the API")