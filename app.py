import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="🌦️ Weather Forecast Pro",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM STYLING ====================
st.markdown("""
<style>
    /* Overall theme */
    :root {
        --primary-color: #1f77b4;
        --secondary-color: #ff7f0e;
        --success-color: #2ca02c;
        --danger-color: #d62728;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom card styling */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Header styling */
    h1 {
        background: linear-gradient(90deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5em !important;
        margin-bottom: 20px;
    }
    
    h2 {
        color: #333;
        border-bottom: 3px solid #667eea;
        padding-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==================== API CONFIG ====================
API_KEY = st.secrets.get("MY_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL = "https://api.openweathermap.org/data/2.5"

# ==================== HELPER FUNCTIONS ====================
@st.cache_data(ttl=600)
def get_current_weather(city):
    """Fetch current weather data from OpenWeatherMap API"""
    try:
        url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json(), None
    except requests.exceptions.RequestException as e:
        return None, f"Error fetching weather: {str(e)}"

@st.cache_data(ttl=600)
def get_forecast_data(city):
    """Fetch 5-day forecast from OpenWeatherMap API"""
    try:
        url = f"{BASE_URL}/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json(), None
    except requests.exceptions.RequestException as e:
        return None, f"Error fetching forecast: {str(e)}"

def parse_forecast(forecast_data):
    """Parse forecast JSON into a clean DataFrame"""
    if not forecast_data or "list" not in forecast_data:
        return None
    
    records = []
    for item in forecast_data["list"]:
        records.append({
            "datetime": datetime.fromtimestamp(item["dt"]),
            "temp": item["main"]["temp"],
            "feels_like": item["main"]["feels_like"],
            "humidity": item["main"]["humidity"],
            "wind_speed": item["wind"]["speed"],
            "description": item["weather"][0]["main"],
            "pressure": item["main"]["pressure"]
        })
    return pd.DataFrame(records)

def get_weather_emoji(description):
    """Return an emoji based on weather description"""
    desc_lower = description.lower()
    emojis = {
        "clear": "☀️",
        "clouds": "☁️",
        "rain": "🌧️",
        "drizzle": "🌦️",
        "thunderstorm": "⛈️",
        "snow": "❄️",
        "mist": "🌫️",
        "smoke": "💨",
        "haze": "🌫️",
        "dust": "💨",
        "fog": "🌫️",
        "sand": "🏜️",
        "ash": "🌋",
        "squall": "💨",
        "tornado": "🌪️"
    }
    for key, emoji in emojis.items():
        if key in desc_lower:
            return emoji
    return "🌤️"

# ==================== HEADER SECTION ====================
st.markdown("# 🌦️ Weather Forecast Pro")
st.markdown("---")

# ==================== SIDEBAR ====================
st.sidebar.markdown("## ⚙️ Settings & Options")
city_input = st.sidebar.text_input("🏙️ Enter City Name", value="London", placeholder="e.g., New York, Tokyo, Paris")
units_option = st.sidebar.radio("📏 Units", ["Metric (°C, m/s)", "Imperial (°F, mph)"], index=0)
refresh_interval = st.sidebar.selectbox("🔄 Cache Duration", ["5 min", "10 min", "30 min"], index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 About")
st.sidebar.markdown("Real-time weather data powered by **OpenWeatherMap API**")
st.sidebar.markdown("*Last updated: 2025-11-14*")

# ==================== MAIN CONTENT ====================
if city_input.strip():
    # Fetch current weather
    weather_data, weather_error = get_current_weather(city_input)
    
    if weather_error:
        st.error(f"❌ {weather_error}")
    elif weather_data and weather_data.get("cod") == 200:
        # Extract weather info
        main_data = weather_data["main"]
        weather_desc = weather_data["weather"][0]["main"]
        wind_data = weather_data["wind"]
        clouds_data = weather_data.get("clouds", {})
        city_name = weather_data.get("name", "")
        country = weather_data.get("sys", {}).get("country", "")
        
        # ==================== CURRENT WEATHER SECTION ====================
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            st.markdown(f"## {city_name}, {country}")
            st.markdown(f"### {get_weather_emoji(weather_desc)} {weather_desc}")
        
        with col2:
            st.markdown("")
        
        with col3:
            st.markdown("")
        
        # Main metrics in a grid
        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
        
        with metric_col1:
            st.metric(label="🌡️ Temperature", value=f"{main_data['temp']}°C", delta=None)
        
        with metric_col2:
            st.metric(label="🤔 Feels Like", value=f"{main_data['feels_like']}°C", delta=None)
        
        with metric_col3:
            st.metric(label="💧 Humidity", value=f"{main_data['humidity']}%", delta=None)
        
        with metric_col4:
            st.metric(label="💨 Wind Speed", value=f"{wind_data.get('speed', 0)} m/s", delta=None)
        
        st.markdown("---")
        
        # Additional details
        details_col1, details_col2, details_col3, details_col4 = st.columns(4)
        
        with details_col1:
            st.info(f"**Pressure**\n{main_data['pressure']} hPa")
        
        with details_col2:
            st.info(f"**Cloud Cover**\n{clouds_data.get('all', 0)}%")
        
        with details_col3:
            st.info(f"**Visibility**\n{weather_data.get('visibility', 'N/A')} m")
        
        with details_col4:
            st.info(f"**UV Index**\n(Not available)")
        
        st.markdown("---")
        
        # ==================== FORECAST SECTION ====================
        st.markdown("## 📈 5-Day Forecast")
        
        forecast_data, forecast_error = get_forecast_data(city_input)
        
        if forecast_error:
            st.warning(f"⚠️ Could not load forecast: {forecast_error}")
        elif forecast_data:
            df_forecast = parse_forecast(forecast_data)
            
            if df_forecast is not None:
                # Temperature trend chart
                fig_temp = go.Figure()
                fig_temp.add_trace(go.Scatter(
                    x=df_forecast['datetime'],
                    y=df_forecast['temp'],
                    mode='lines+markers',
                    name='Temperature',
                    line=dict(color='#ff7f0e', width=3),
                    marker=dict(size=8)
                ))
                fig_temp.add_trace(go.Scatter(
                    x=df_forecast['datetime'],
                    y=df_forecast['feels_like'],
                    mode='lines',
                    name='Feels Like',
                    line=dict(color='#d62728', width=2, dash='dash')
                ))
                fig_temp.update_layout(
                    title="Temperature Trend",
                    xaxis_title="Date & Time",
                    yaxis_title="Temperature (°C)",
                    hovermode='x unified',
                    template='plotly_white',
                    height=400
                )
                st.plotly_chart(fig_temp, use_container_width=True)
                
                # Humidity bar chart
                fig_humidity = go.Figure()
                fig_humidity.add_trace(go.Bar(
                    x=df_forecast['datetime'],
                    y=df_forecast['humidity'],
                    name='Humidity',
                    marker_color='#1f77b4'
                ))
                fig_humidity.update_layout(
                    title="Humidity Levels",
                    xaxis_title="Date & Time",
                    yaxis_title="Humidity (%)",
                    hovermode='x',
                    template='plotly_white',
                    height=350
                )
                st.plotly_chart(fig_humidity, use_container_width=True)
                
                # Forecast table
                with st.expander("📋 Detailed Forecast Data"):
                    display_df = df_forecast.copy()
                    display_df['datetime'] = display_df['datetime'].dt.strftime('%Y-%m-%d %H:%M')
                    st.dataframe(display_df, use_container_width=True)
    else:
        st.error(f"❌ City '{city_input}' not found. Please check the spelling and try again.")
else:
    st.info("👈 Enter a city name in the sidebar to get started!")

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><small>Data from OpenWeatherMap API | Built with Streamlit</small></p>
</div>
""", unsafe_allow_html=True)
