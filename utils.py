"""
Utility functions for WeatherHub application
"""

from datetime import datetime, timedelta
import streamlit as st
from config import WEATHER_ICONS, COLORS, STYLES, UV_INDEX_LEVELS


def get_weather_icon(condition: str) -> str:
    """
    Get emoji icon for weather condition
    """
    for key, icon in WEATHER_ICONS.items():
        if key.lower() in condition.lower():
            return icon
    return "🌤️"  # Default icon


def format_temperature(temp: float, unit: str = "°C") -> str:
    """
    Format temperature value with unit
    """
    return f"{round(temp)}{unit}"


def format_time(timestamp: datetime, format: str = "%H:%M") -> str:
    """
    Format datetime to string
    """
    if isinstance(timestamp, int):
        timestamp = datetime.fromtimestamp(timestamp)
    return timestamp.strftime(format)


def calculate_uv_level(uv_index: float) -> str:
    """
    Get UV index level text
    """
    if uv_index < 3:
        return "Low"
    elif uv_index < 6:
        return "Moderate"
    elif uv_index < 8:
        return "High"
    elif uv_index < 11:
        return "Very High"
    else:
        return "Extreme"


def get_uv_color(uv_index: float) -> str:
    """
    Get color for UV index
    """
    for level, data in UV_INDEX_LEVELS.items():
        if uv_index >= data['range'][0] and uv_index < data['range'][1]:
            return data['color']
    return "rgb(150, 0, 255)"  # Extreme


def calculate_feels_like(temp: float, humidity: float, wind_speed: float) -> float:
    """
    Calculate wind chill/heat index
    Simplified calculation
    """
    if temp < 10:
        # Wind chill formula
        return temp - (wind_speed * 0.2)
    else:
        # Heat index approximation
        return temp + (humidity * 0.05)


def get_visibility_description(visibility: float) -> str:
    """
    Get visibility description
    """
    if visibility >= 10:
        return "Excellent"
    elif visibility >= 5:
        return "Good"
    elif visibility >= 1:
        return "Moderate"
    elif visibility > 0:
        return "Poor"
    else:
        return "Very Poor"


def get_wind_direction(degree: float) -> str:
    """
    Convert wind degree to direction
    """
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = round(degree / 22.5) % 16
    return directions[index]


def format_sunrise_sunset(timestamp: datetime) -> str:
    """
    Format sunrise/sunset time
    """
    return format_time(timestamp, "%H:%M")


def calculate_daylight_hours(sunrise: datetime, sunset: datetime) -> float:
    """
    Calculate hours of daylight
    """
    delta = sunset - sunrise
    return delta.total_seconds() / 3600


def get_color_for_temp(temp: float) -> str:
    """
    Get color based on temperature
    """
    if temp < 0:
        return "rgb(100, 200, 255)"  # Blue - cold
    elif temp < 10:
        return "rgb(150, 200, 255)"  # Light blue - cool
    elif temp < 20:
        return "rgb(200, 200, 0)"  # Yellow - mild
    elif temp < 30:
        return "rgb(255, 150, 50)"  # Orange - warm
    else:
        return "rgb(255, 50, 50)"  # Red - hot


def format_decimal(value: float, decimals: int = 1) -> str:
    """
    Format decimal number
    """
    return f"{value:.{decimals}f}"


def get_pressure_description(pressure: float) -> str:
    """
    Get pressure description
    """
    if pressure > 1020:
        return "High - Stable Weather"
    elif pressure > 1010:
        return "Normal"
    elif pressure > 990:
        return "Low - Unstable Weather"
    else:
        return "Very Low - Storm Risk"


def get_humidity_description(humidity: float) -> str:
    """
    Get humidity description
    """
    if humidity < 30:
        return "Dry"
    elif humidity < 50:
        return "Comfortable"
    elif humidity < 70:
        return "Humid"
    else:
        return "Very Humid"


def create_glass_card_html(content: str, title: str = None, height: str = "auto") -> str:
    """
    Generate HTML for glassmorphic card
    """
    html = f"""
    <div class='glass-card' style='height: {height};'>
    """
    
    if title:
        html += f"<h3 style='margin-top: 0;'>{title}</h3>"
    
    html += f"{content}</div>"
    
    return html


def render_metric(label: str, value: str, icon: str = None) -> str:
    """
    Render a metric display
    """
    icon_html = f"<div style='font-size: 32px; margin: 10px 0;'>{icon}</div>" if icon else ""
    
    return f"""
    <div class='glass-card-dark' style='text-align: center;'>
        <p class='metric-label'>{label}</p>
        {icon_html}
        <div class='metric-value'>{value}</div>
    </div>
    """


def get_forecast_icon(condition: str) -> str:
    """
    Get forecast icon with emoji
    """
    condition = condition.lower()
    
    if "clear" in condition or "sunny" in condition:
        return "☀️"
    elif "cloud" in condition:
        return "☁️"
    elif "rain" in condition:
        return "🌧️"
    elif "storm" in condition or "thunder" in condition:
        return "⛈️"
    elif "snow" in condition:
        return "❄️"
    elif "wind" in condition:
        return "🌪️"
    elif "fog" in condition or "mist" in condition:
        return "🌫️"
    else:
        return "🌤️"


def convert_temperature(temp: float, from_unit: str, to_unit: str) -> float:
    """
    Convert temperature between units
    """
    if from_unit == to_unit:
        return temp
    
    if from_unit == "°C" and to_unit == "°F":
        return (temp * 9/5) + 32
    elif from_unit == "°F" and to_unit == "°C":
        return (temp - 32) * 5/9
    else:
        return temp


def convert_wind_speed(speed: float, from_unit: str, to_unit: str) -> float:
    """
    Convert wind speed between units
    """
    if from_unit == to_unit:
        return speed
    
    conversions = {
        ("km/h", "mph"): 0.621371,
        ("mph", "km/h"): 1.60934,
        ("km/h", "m/s"): 0.27778,
        ("m/s", "km/h"): 3.6,
        ("mph", "m/s"): 0.44704,
        ("m/s", "mph"): 2.23694,
        ("km/h", "knots"): 0.539957,
        ("knots", "km/h"): 1.852,
    }
    
    key = (from_unit, to_unit)
    if key in conversions:
        return speed * conversions[key]
    
    return speed


def get_air_quality_description(aqi: int) -> str:
    """
    Get air quality description
    """
    descriptions = {
        1: "Good - Air quality is satisfactory",
        2: "Fair - Acceptable air quality",
        3: "Moderate - Some pollution",
        4: "Poor - Unhealthy air",
        5: "Very Poor - Very unhealthy air",
    }
    return descriptions.get(aqi, "Unknown")


def format_location(city: str, country: str = None) -> str:
    """
    Format location string
    """
    if country:
        return f"{city}, {country}"
    return city


def calculate_wind_chill(temp: float, wind_speed: float) -> float:
    """
    Calculate wind chill temperature (Celsius)
    """
    if temp >= 10:
        return temp  # No wind chill above 10°C
    
    # Wind chill formula: T_wc = T - (1.41671 - 0.04694 * v) * (10.29 + 6.1355 * v^0.16 - T)
    # Simplified version:
    return temp - (0.2 * wind_speed)


def get_week_day_name(offset: int) -> str:
    """
    Get day name for given offset from today
    """
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    date = datetime.now() + timedelta(days=offset)
    return days[date.weekday()]


def get_month_name(month: int) -> str:
    """
    Get month name from number
    """
    months = ["", "January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return months[month] if 1 <= month <= 12 else ""


def format_date_relative(date: datetime) -> str:
    """
    Format date as relative (e.g., "Today", "Tomorrow", "Monday")
    """
    today = datetime.now().date()
    delta = (date.date() - today).days
    
    if delta == 0:
        return "Today"
    elif delta == 1:
        return "Tomorrow"
    elif delta == -1:
        return "Yesterday"
    else:
        return date.strftime("%A")


def create_progress_bar(value: float, max_value: float, label: str = "") -> str:
    """
    Create HTML progress bar
    """
    percentage = (value / max_value) * 100
    
    return f"""
    <div style='margin: 10px 0;'>
        <p style='margin: 0 0 5px 0; color: rgba(255,255,255,0.8);'>{label}</p>
        <div style='background: rgba(255,255,255,0.1); border-radius: 10px; height: 20px; overflow: hidden;'>
            <div style='background: rgba(255,200,0,0.8); width: {percentage}%; height: 100%; transition: width 0.3s;'></div>
        </div>
        <p style='margin: 5px 0 0 0; color: rgba(255,255,255,0.6); font-size: 12px;'>{value:.1f} / {max_value}</p>
    </div>
    """


@st.cache_data(ttl=600)
def get_cached_data(key: str, fetch_func):
    """
    Cached data fetcher
    """
    return fetch_func()


# Export all functions
__all__ = [
    'get_weather_icon',
    'format_temperature',
    'format_time',
    'calculate_uv_level',
    'get_uv_color',
    'calculate_feels_like',
    'get_visibility_description',
    'get_wind_direction',
    'format_sunrise_sunset',
    'calculate_daylight_hours',
    'get_color_for_temp',
    'format_decimal',
    'get_pressure_description',
    'get_humidity_description',
    'create_glass_card_html',
    'render_metric',
    'get_forecast_icon',
    'convert_temperature',
    'convert_wind_speed',
    'get_air_quality_description',
    'format_location',
    'calculate_wind_chill',
    'get_week_day_name',
    'get_month_name',
    'format_date_relative',
    'create_progress_bar',
    'get_cached_data',
]
