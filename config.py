"""
Configuration file for WeatherHub
Customize colors, fonts, and behavior
"""

# ===== COLOR SCHEME =====
COLORS = {
    # Gradient background colors
    "gradient_start": "#667eea",
    "gradient_end": "#764ba2",
    
    # Text colors
    "text_primary": "white",
    "text_secondary": "rgba(255,255,255,0.7)",
    "text_muted": "rgba(255,255,255,0.6)",
    "text_dark": "rgba(255,255,255,0.5)",
    
    # Card colors
    "card_bg": "rgba(255, 255, 255, 0.1)",
    "card_border": "rgba(255, 255, 255, 0.2)",
    "card_bg_dark": "rgba(255, 255, 255, 0.08)",
    "card_border_dark": "rgba(255, 255, 255, 0.15)",
    
    # Chart colors
    "chart_line": "rgba(255,255,255,0.8)",
    "chart_fill_temp": "rgba(255,200,0,0.2)",
    "chart_marker_temp": "rgba(255,200,0,0.8)",
    "chart_line_high": "rgba(255,150,50,0.8)",
    "chart_line_low": "rgba(100,200,255,0.8)",
    "chart_fill_range": "rgba(150,200,255,0.2)",
    
    # UV Index colors
    "uv_low": "rgba(50,255,50,0.2)",
    "uv_moderate": "rgba(255,255,50,0.2)",
    "uv_high": "rgba(255,150,50,0.2)",
    "uv_very_high": "rgba(255,50,50,0.2)",
    
    # Grid colors
    "grid_light": "rgba(255,255,255,0.1)",
    "grid_dark": "rgba(0,0,0,0.1)",
}

# ===== STYLING =====
STYLES = {
    # Border radius values (pixels)
    "border_radius_large": "20px",
    "border_radius_medium": "15px",
    "border_radius_small": "10px",
    
    # Padding values (pixels)
    "padding_large": "20px",
    "padding_medium": "15px",
    "padding_small": "10px",
    
    # Font sizes
    "font_size_large": "32px",
    "font_size_medium": "18px",
    "font_size_normal": "14px",
    "font_size_small": "12px",
    
    # Shadows
    "shadow_light": "0 8px 32px rgba(0, 0, 0, 0.1)",
    "shadow_medium": "0 8px 32px rgba(0, 0, 0, 0.15)",
    "shadow_dark": "0 10px 40px rgba(0, 0, 0, 0.2)",
    
    # Blur effect
    "backdrop_blur": "blur(10px)",
    "backdrop_blur_light": "blur(5px)",
    "backdrop_blur_strong": "blur(15px)",
}

# ===== LAYOUT =====
LAYOUT = {
    # Page layout
    "page_layout": "wide",
    "sidebar_state": "expanded",
    
    # Container widths
    "main_width": "100%",
    "sidebar_width": "300px",
    
    # Spacing
    "section_margin": "30px",
    "widget_margin": "10px",
}

# ===== WEATHER ICONS MAPPING =====
WEATHER_ICONS = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Cloudy": "⛅",
    "Drizzle": "🌦️",
    "Rain": "🌧️",
    "Rainy": "⛈️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "🌫️",
    "Sunny": "🌞",
    "Partly Cloudy": "🌤️",
}

# ===== NAVIGATION MENU =====
MENU_ITEMS = {
    "🏠 Dashboard": "dashboard",
    "📍 Location": "location",
    "📊 Analytics": "analytics",
    "⚙️ Settings": "settings",
    "ℹ️ About": "about",
}

# ===== TEMPERATURE UNITS =====
TEMPERATURE_UNITS = {
    "Celsius": {"symbol": "°C", "api_unit": "metric"},
    "Fahrenheit": {"symbol": "°F", "api_unit": "imperial"},
}

# ===== WIND SPEED UNITS =====
WIND_UNITS = {
    "km/h": "metric",
    "m/s": "metric",
    "mph": "imperial",
    "knots": "nautical",
}

# ===== PRESSURE UNITS =====
PRESSURE_UNITS = {
    "mb": 1,
    "hPa": 1,
    "inHg": 29.92 / 1013.25,
}

# ===== DEFAULT VALUES =====
DEFAULTS = {
    "city": "London",
    "temp_unit": "°C",
    "wind_unit": "km/h",
    "pressure_unit": "mb",
    "forecast_days": 5,
    "cache_duration": 600,  # 10 minutes in seconds
    "sidebar_collapsed": False,
}

# ===== API CONFIGURATION =====
API_CONFIG = {
    # OpenWeatherMap API
    "openweathermap": {
        "base_url": "https://api.openweathermap.org/data/2.5",
        "api_key": "YOUR_API_KEY_HERE",  # Replace with your key
        "timeout": 5,
    },
    
    # Weather API alternative
    "weatherapi": {
        "base_url": "https://api.weatherapi.com/v1",
        "api_key": "YOUR_API_KEY_HERE",  # Replace with your key
        "timeout": 5,
    },
}

# ===== CHART CONFIGURATION =====
CHART_CONFIG = {
    "show_toolbar": False,
    "responsive": True,
    "height": 400,
    "hovermode": "x unified",
    "template": "plotly_dark",
}

# ===== PAGE METADATA =====
PAGE_METADATA = {
    "title": "WeatherHub",
    "icon": "🌤️",
    "description": "Modern Weather Forecasting Application",
    "author": "Your Name",
    "version": "1.0.0",
}

# ===== LOCATIONS =====
SAVED_LOCATIONS = [
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "Paris", "lat": 48.8566, "lon": 2.3522},
    {"name": "Berlin", "lat": 52.5200, "lon": 13.4050},
    {"name": "New York", "lat": 40.7128, "lon": -74.0060},
    {"name": "Tokyo", "lat": 35.6762, "lon": 139.6503},
    {"name": "Sydney", "lat": -33.8688, "lon": 151.2093},
    {"name": "Dubai", "lat": 25.2048, "lon": 55.2708},
    {"name": "Singapore", "lat": 1.3521, "lon": 103.8198},
]

# ===== THEME PRESETS =====
THEME_PRESETS = {
    "ocean": {
        "gradient_start": "#0066cc",
        "gradient_end": "#0099ff",
    },
    "sunset": {
        "gradient_start": "#ff6b35",
        "gradient_end": "#f7931e",
    },
    "forest": {
        "gradient_start": "#134e5e",
        "gradient_end": "#71b280",
    },
    "purple": {
        "gradient_start": "#667eea",
        "gradient_end": "#764ba2",
    },
    "pink": {
        "gradient_start": "#ff6b9d",
        "gradient_end": "#c44569",
    },
}

# ===== UV INDEX LEVELS =====
UV_INDEX_LEVELS = {
    "Low": {"range": (0, 2), "color": "rgb(50, 255, 50)", "advice": "No protection required"},
    "Moderate": {"range": (3, 5), "color": "rgb(255, 255, 50)", "advice": "Wear sunscreen"},
    "High": {"range": (6, 7), "color": "rgb(255, 150, 50)", "advice": "Seek shade during midday"},
    "Very High": {"range": (8, 10), "color": "rgb(255, 50, 50)", "advice": "Avoid sun exposure"},
    "Extreme": {"range": (11, 16), "color": "rgb(150, 0, 255)", "advice": "Stay indoors"},
}

# ===== AIR QUALITY LEVELS =====
AIR_QUALITY_LEVELS = {
    "Good": {"value": 1, "color": "rgb(0, 255, 0)"},
    "Fair": {"value": 2, "color": "rgb(255, 255, 0)"},
    "Moderate": {"value": 3, "color": "rgb(255, 150, 0)"},
    "Poor": {"value": 4, "color": "rgb(255, 0, 0)"},
    "Very Poor": {"value": 5, "color": "rgb(150, 0, 0)"},
}

# ===== WIND DIRECTIONS =====
WIND_DIRECTIONS = {
    "N": (348.75, 360) + (0, 11.25),
    "NE": (11.25, 33.75),
    "E": (78.75, 101.25),
    "SE": (101.25, 123.75),
    "S": (168.75, 191.25),
    "SW": (213.75, 236.25),
    "W": (258.75, 281.25),
    "NW": (303.75, 326.25),
}


def get_color(color_name: str) -> str:
    """Get color from color scheme"""
    return COLORS.get(color_name, COLORS["text_primary"])


def get_style(style_name: str) -> str:
    """Get style value"""
    return STYLES.get(style_name, "")


def get_default(key: str):
    """Get default configuration value"""
    return DEFAULTS.get(key, None)
