"""
Optional: Weather API integration module
Add your API key and uncomment to use real weather data
"""

import requests
from datetime import datetime, timedelta
import json

class WeatherAPI:
    """
    Integration with OpenWeatherMap API
    Get free API key at: https://openweathermap.org/api
    """
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"
        
    def get_current_weather(self, city: str, units: str = "metric"):
        """
        Get current weather data for a city
        """
        try:
            endpoint = f"{self.base_url}/weather"
            params = {
                "q": city,
                "appid": self.api_key,
                "units": units
            }
            
            response = requests.get(endpoint, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            return {
                "city": data['name'],
                "country": data['sys']['country'],
                "temp": round(data['main']['temp']),
                "feels_like": round(data['main']['feels_like']),
                "humidity": data['main']['humidity'],
                "pressure": data['main']['pressure'],
                "wind_speed": round(data['wind']['speed']),
                "visibility": round(data['visibility'] / 1000),
                "condition": data['weather'][0]['main'],
                "description": data['weather'][0]['description'],
                "icon": data['weather'][0]['icon'],
                "clouds": data['clouds']['all'],
                "sunrise": datetime.fromtimestamp(data['sys']['sunrise']),
                "sunset": datetime.fromtimestamp(data['sys']['sunset']),
                "uv_index": self._get_uv_index(data['coord']['lat'], data['coord']['lon']),
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def get_forecast(self, city: str, days: int = 5, units: str = "metric"):
        """
        Get forecast data for a city
        """
        try:
            endpoint = f"{self.base_url}/forecast"
            params = {
                "q": city,
                "appid": self.api_key,
                "units": units,
                "cnt": days * 8  # 8 forecasts per day (3-hour intervals)
            }
            
            response = requests.get(endpoint, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            forecast_list = []
            seen_days = set()
            
            for item in data['list']:
                dt = datetime.fromtimestamp(item['dt'])
                day = dt.date()
                
                if day not in seen_days and len(forecast_list) < days:
                    seen_days.add(day)
                    forecast_list.append({
                        "day": dt.strftime("%A"),
                        "date": dt.strftime("%d %B"),
                        "high": round(item['main']['temp_max']),
                        "low": round(item['main']['temp_min']),
                        "condition": item['weather'][0]['main'],
                        "icon": item['weather'][0]['icon'],
                        "description": item['weather'][0]['description'],
                        "humidity": item['main']['humidity'],
                        "wind_speed": round(item['wind']['speed']),
                        "precipitation": item.get('rain', {}).get('3h', 0),
                    })
            
            return forecast_list
        except requests.exceptions.RequestException as e:
            print(f"Error fetching forecast data: {e}")
            return []
    
    def get_uv_index(self, lat: float, lon: float):
        """
        Get UV index for a location
        """
        try:
            endpoint = f"{self.base_url}/uvi"
            params = {
                "lat": lat,
                "lon": lon,
                "appid": self.api_key
            }
            
            response = requests.get(endpoint, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            return round(data['value'])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching UV index: {e}")
            return 0
    
    def _get_uv_index(self, lat: float, lon: float):
        """Internal method to get UV index"""
        return self.get_uv_index(lat, lon)


class WeatherDataCache:
    """
    Simple caching system for weather data
    """
    
    def __init__(self, cache_duration: int = 600):  # 10 minutes default
        self.cache = {}
        self.cache_duration = cache_duration
        self.timestamps = {}
    
    def get(self, key: str):
        """Get cached data if still valid"""
        if key in self.cache:
            elapsed = (datetime.now() - self.timestamps[key]).total_seconds()
            if elapsed < self.cache_duration:
                return self.cache[key]
            else:
                del self.cache[key]
                del self.timestamps[key]
        return None
    
    def set(self, key: str, value):
        """Cache data with timestamp"""
        self.cache[key] = value
        self.timestamps[key] = datetime.now()
    
    def clear(self):
        """Clear all cache"""
        self.cache.clear()
        self.timestamps.clear()


# Usage example in app.py:
"""
from weather_api import WeatherAPI, WeatherDataCache

# Initialize API (get free key from openweathermap.org)
API_KEY = "your_api_key_here"
weather_api = WeatherAPI(API_KEY)
cache = WeatherDataCache(cache_duration=600)  # 10 minutes

# Get current weather
current = weather_api.get_current_weather("London")
if current:
    st.write(f"Temperature: {current['temp']}°C")

# Get forecast
forecast = weather_api.get_forecast("London", days=5)
for day_forecast in forecast:
    st.write(f"{day_forecast['day']}: {day_forecast['high']}°C / {day_forecast['low']}°C")
"""
