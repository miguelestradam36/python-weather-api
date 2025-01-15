import pytest

def test_connection():
    """
    Test connection to the API (Free Weather API)
    """
    openmeteo_requests =  __import__('openmeteo_requests')
    requests_cache =  __import__('requests_cache')
    pandas =  __import__('pandas')
    retry_requests =  __import__('retry_requests')
    
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry_requests.retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    longitude_ = "10"
    latitude_ = "10"
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude_,
        "longitude": longitude_,
        "hourly": "temperature_2m"
    }
    assert openmeteo.weather_api(url, params=params)