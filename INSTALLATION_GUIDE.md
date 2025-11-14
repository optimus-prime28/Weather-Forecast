# 🌤️ WeatherHub - Complete Installation & Usage Guide

## 📋 Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation Steps](#installation-steps)
3. [Running the App](#running-the-app)
4. [Features Guide](#features-guide)
5. [Customization](#customization)
6. [API Integration](#api-integration)
7. [Troubleshooting](#troubleshooting)
8. [File Reference](#file-reference)

---

## 🖥️ System Requirements

### Minimum Requirements
- **Operating System**: Windows 7+, macOS 10.12+, Linux
- **Python**: 3.8 or higher
- **RAM**: 2GB minimum (4GB recommended)
- **Disk Space**: 500MB free space
- **Browser**: Chrome, Edge, Firefox, or Safari (latest versions)

### Verify Python Installation
```powershell
python --version
pip --version
```

Should show Python 3.8+ and pip installed.

---

## 📦 Installation Steps

### Step 1: Navigate to Project Directory

**On Windows (PowerShell):**
```powershell
cd c:\Users\prans\sem1_projectai
```

**On macOS/Linux:**
```bash
cd ~/sem1_projectai
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

✅ Your terminal should show `(venv)` prefix when active

### Step 3: Install Dependencies

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

**Expected Output:**
```
Successfully installed streamlit-1.28.1
Successfully installed plotly-5.17.0
Successfully installed pandas-2.0.3
Successfully installed numpy-1.24.3
Successfully installed requests-2.31.0
Successfully installed pillow-10.0.0
Successfully installed folium-0.14.0
Successfully installed streamlit-folium-0.15.0
```

### Step 4: Verify Installation

Run the verification script:

```powershell
python verify_setup.py
```

**Expected Output:**
```
========================================
✓ Checking Python version...
  Python version: 3.11.5
  ✅ Python 3.8+ detected

✓ Checking required packages...
  ✅ streamlit installed
  ✅ plotly installed
  ✅ pandas installed
  ... (all packages should show ✅)

✓ Checking project files...
  ✅ app.py
  ✅ config.py
  ✅ weather_api.py
  ... (all files should show ✅)

========================================
📊 Verification Summary

✅ All checks passed!

🚀 You can now run:
   streamlit run app.py
========================================
```

---

## 🚀 Running the Application

### Basic Command

```powershell
streamlit run app.py
```

### What Happens
1. Streamlit starts a local server
2. Opens automatically in your default browser
3. Shows: `http://localhost:8501`
4. Displays: "WeatherHub" application

### Options
```powershell
# Run with custom port
streamlit run app.py --server.port 8502

# Run with logger level
streamlit run app.py --logger.level=error

# Run without opening browser
streamlit run app.py --server.headless true

# Run in demo mode
streamlit run app.py --logger.level=warning
```

### Stopping the App
Press `Ctrl + C` in PowerShell terminal

---

## 🎨 Features Guide

### Dashboard (Home)

#### Current Weather Card
- **Location**: Displayed in header
- **Temperature**: Large format (e.g., "22°C")
- **Condition**: "Partly Cloudy" text
- **Feels Like**: Additional temperature info
- **Humidity**: Percentage display
- **Wind**: Speed and unit

**Actions:**
- Change temperature unit (°C / °F)
- Change wind unit (km/h / mph)
- Select different city

#### 4-Day Forecast
Shows 4 cards with:
- Day name (Tomorrow, Wednesday, etc.)
- Weather icon (🌞⛅🌧️🌤️)
- High/Low temperatures
- Weather description

#### Daily Report Chart
- X-axis: Hours (0-24)
- Y-axis: Temperature in °C
- Orange line with markers
- Filled area underneath
- Hover for exact values

#### UV Index Gauge
- Circular gauge chart
- Color zones: Green → Red
- Center value (0-11 scale)
- Real-time update
- Safety level indicator

#### Sunrise/Sunset Widget
- Sunrise time (e.g., 06:45)
- Sunset time (e.g., 18:30)
- Total daylight hours
- Weather emoji icons

#### Detailed Metrics Grid
Four cards showing:
1. **Pressure**: mb (millibar)
2. **Visibility**: km distance
3. **Dew Point**: °C temperature
4. **Wind Gust**: km/h speed

#### Weekly Temperature Trend
- 7-day forecast
- High temps (orange line)
- Low temps (blue line)
- Filled area between
- Day labels
- Interactive legend

#### Weather Map
- Global map view
- Location markers (5 cities)
- Temperature color gradient
- Hover information
- Zoom/pan controls

### Location Settings Page
- Input field to add new location
- Button to save location
- List of saved locations
- Quick access to favorites

### Analytics Page
- Monthly average temperatures
- Rainfall patterns (bar chart)
- Dual-axis visualization
- Trend analysis

### Settings Page
- Temperature unit toggle
- Wind speed unit toggle
- Alert notifications checkbox
- Dark mode indicator

### About Page
- App description
- Feature list
- Technology stack
- Version information

---

## 🎨 Customization

### Change Colors

Edit `config.py`:

```python
COLORS = {
    "gradient_start": "#667eea",  # Change from purple
    "gradient_end": "#764ba2",    # Change to other color
}
```

**Popular Gradients:**
```python
# Ocean Blue
"gradient_start": "#0066cc"
"gradient_end": "#0099ff"

# Sunset
"gradient_start": "#ff6b35"
"gradient_end": "#f7931e"

# Forest Green
"gradient_start": "#134e5e"
"gradient_end": "#71b280"

# Pink
"gradient_start": "#ff6b9d"
"gradient_end": "#c44569"
```

### Change Font Sizes

Edit `config.py`:

```python
STYLES = {
    "font_size_large": "32px",    # Main temperature
    "font_size_medium": "18px",   # Secondary text
    "font_size_normal": "14px",   # Normal text
}
```

Or directly in `app.py` CSS:

```python
.metric-value {
    font-size: 32px;  # Change this
}
```

### Change Location Defaults

Edit `config.py`:

```python
DEFAULTS = {
    "city": "London",  # Default city
    "temp_unit": "°C",
    "wind_unit": "km/h",
}
```

Or edit sidebar in `app.py`:

```python
city = st.text_input(
    "City name",
    "London",  # Change this
    placeholder="Enter city name"
)
```

### Add More Locations

Edit `config.py`:

```python
SAVED_LOCATIONS = [
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "Paris", "lat": 48.8566, "lon": 2.3522},
    # Add more here
]
```

### Change Chart Heights

Edit `app.py`:

```python
fig_temp.update_layout(
    height=300,  # Change this value (in pixels)
)

fig_weekly.update_layout(
    height=400,  # Change this value
)

fig_map.update_layout(
    height=500,  # Change this value
)
```

---

## 🔌 API Integration

### Get OpenWeatherMap API Key

1. Visit: https://openweathermap.org/api
2. Sign up for free account
3. Generate API key from dashboard
4. Copy your API key

### Add API Key to Application

**Option 1: Direct Configuration**
Edit `config.py`:

```python
API_CONFIG = {
    "openweathermap": {
        "base_url": "https://api.openweathermap.org/data/2.5",
        "api_key": "your_api_key_here",  # Paste your key
        "timeout": 5,
    },
}
```

**Option 2: Environment Variable (Recommended)**

Create `.env` file:
```
OPENWEATHERMAP_API_KEY=your_api_key_here
```

Update `app.py`:
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHERMAP_API_KEY")
```

### Use Real Weather Data

In `app.py`, replace sample data:

```python
from weather_api import WeatherAPI

api = WeatherAPI(api_key)

# Get current weather
current_weather = api.get_current_weather(city)

# Get forecast
forecast_data = api.get_forecast(city, days=4)
```

### Example Implementation

```python
if current_weather:
    st.markdown(f"""
    <div class='glass-card'>
        <h1>{current_weather['city']}</h1>
        <p>{current_weather['temp']}°C</p>
        <p>{current_weather['condition']}</p>
    </div>
    """, unsafe_allow_html=True)
```

---

## 🐛 Troubleshooting

### Issue: "streamlit command not found"
**Solution:**
```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Then run
streamlit run app.py
```

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution:**
```powershell
pip install streamlit
# Or reinstall all dependencies
pip install -r requirements.txt
```

### Issue: Port 8501 already in use
**Solution:**
```powershell
# Use different port
streamlit run app.py --server.port 8502
```

### Issue: Charts not displaying
**Solution:**
```powershell
# Update Plotly
pip install --upgrade plotly

# Clear cache
streamlit cache clear

# Restart application
```

### Issue: Sidebar not visible
**Solution:**
- Check browser window is wide enough
- Refresh page (F5)
- Check `initial_sidebar_state="expanded"` in `app.py`

### Issue: Styling looks broken
**Solution:**
```powershell
# Clear browser cache (Ctrl+Shift+Delete)
# Or use incognito/private window
# Ensure unsafe_allow_html=True in st.markdown()
```

### Issue: API errors
**Solution:**
1. Verify API key is correct
2. Check API key has proper permissions
3. Check rate limits (free tier: 60 calls/minute)
4. Verify internet connection
5. Test with curl:
   ```powershell
   curl "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_KEY"
   ```

### Issue: Slow performance
**Solution:**
```python
# Add caching
@st.cache_data(ttl=600)
def get_weather(city):
    return api.get_current_weather(city)

# Or reduce chart complexity
fig.update_layout(displayModeBar=False)
```

---

## 📁 File Reference

### app.py (20KB)
**Main application file**

**Contains:**
- Streamlit page configuration
- Custom CSS/glassmorphism styling
- Sidebar navigation
- Dashboard widgets
- All pages (Dashboard, Location, Analytics, Settings, About)
- Weather card components
- Chart visualizations
- Map integration

**Key Functions:**
- Page layout setup
- CSS styling
- Navigation menu
- Widget rendering
- Chart creation

**Edit this file for:**
- UI changes
- Adding new pages
- Modifying layouts
- Chart customization

---

### config.py (7KB)
**Configuration and constants**

**Contains:**
- Color schemes
- Font sizes and styles
- Default values
- API configuration
- Location data
- Theme presets
- Wind direction mappings
- UV index levels
- Air quality levels

**Edit this file for:**
- Color changes
- Font customization
- API keys
- Default settings
- Location management
- Theme selection

---

### weather_api.py (6KB)
**Weather API integration**

**Contains:**
- WeatherAPI class
- Weather data fetching
- Forecast retrieval
- UV index calculation
- Data caching system
- Error handling

**Use this file for:**
- Current weather data
- 5-day forecast
- UV index data
- Temperature conversions
- API error handling

**Methods:**
```python
api.get_current_weather(city)  # Get current conditions
api.get_forecast(city)          # Get 5-day forecast
api.get_uv_index(lat, lon)      # Get UV index
```

---

### utils.py (10KB)
**Utility functions and helpers**

**Contains:**
- Format functions
- Icon getters
- Calculation helpers
- Unit conversion functions
- HTML generators
- Caching decorators

**Use this file for:**
- Formatting data
- Converting units
- Getting icons
- Calculating values
- Creating components

**Example Functions:**
```python
get_weather_icon(condition)          # Get emoji icon
format_temperature(temp, unit)       # Format temp
calculate_feels_like(temp, humidity) # Calc feels-like
convert_temperature(temp, from, to)  # Convert units
```

---

### requirements.txt (141B)
**Python dependencies**

**Contains:**
- streamlit 1.28.1
- plotly 5.17.0
- pandas 2.0.3
- numpy 1.24.3
- requests 2.31.0
- pillow 10.0.0
- folium 0.14.0
- streamlit-folium 0.15.0

**Install:**
```powershell
pip install -r requirements.txt
```

---

### README.md (5.6KB)
**Comprehensive documentation**

**Contains:**
- Feature overview
- Installation instructions
- Project structure
- Customization guide
- API integration info
- Troubleshooting tips
- Technology stack
- License information

---

### QUICKSTART.md (7.9KB)
**Quick start and setup guide**

**Contains:**
- 5-minute setup
- Features overview
- Dashboard components
- Customization tips
- Common tasks
- Performance optimization
- Troubleshooting table

---

### PROJECT_SUMMARY.md (13KB)
**Complete project summary**

**Contains:**
- Project overview
- Feature checklist
- Design specifications
- Component breakdown
- Color scheme documentation
- Performance notes
- Future enhancements
- Support information

---

### verify_setup.py (3KB)
**Setup verification script**

**Contains:**
- Python version check
- Package verification
- File verification
- Installation diagnostics
- Setup instructions

**Run:**
```powershell
python verify_setup.py
```

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| Total Files | 9 |
| Total Code | ~50 KB |
| Python Files | 5 |
| Documentation | 4 files |
| Lines of Code | ~1500 |
| CSS Lines | ~150 |
| Functions | 50+ |
| UI Components | 20+ |
| Chart Types | 5 |
| Pages | 5 |
| Responsive Breakpoints | 3 |

---

## ✅ Verification Checklist

After installation, verify:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] All dependencies installed
- [ ] verify_setup.py runs successfully
- [ ] app.py starts without errors
- [ ] Browser opens automatically
- [ ] Dashboard displays correctly
- [ ] Sidebar navigation works
- [ ] All pages load
- [ ] Charts render properly

---

## 📞 Support Resources

| Issue | Resource |
|-------|----------|
| Installation | QUICKSTART.md |
| Features | README.md |
| Customization | config.py documentation |
| API | weather_api.py docstrings |
| Utilities | utils.py docstrings |
| General | PROJECT_SUMMARY.md |

---

## 🎓 Learning Path

**Beginner:**
1. Read QUICKSTART.md
2. Install and run app
3. Explore dashboard

**Intermediate:**
4. Read README.md
5. Edit colors in config.py
6. Modify chart settings
7. Customize fonts

**Advanced:**
8. Integrate real API
9. Add database
10. Create custom widgets
11. Deploy to production

---

## 🚀 Next Steps

1. **Installation Complete?**
   - Run `streamlit run app.py`

2. **Want Real Weather Data?**
   - Get API key from openweathermap.org
   - Add to config.py
   - Use weather_api.py functions

3. **Want to Customize?**
   - Edit config.py for colors
   - Edit app.py for layout
   - Edit CSS for styling

4. **Ready to Deploy?**
   - Use Streamlit Cloud (free tier)
   - Or deploy to Heroku/Vercel
   - See README.md for details

---

## 🎉 You're Ready!

Your WeatherHub application is fully installed and ready to use.

**Start now:**
```powershell
cd c:\Users\prans\sem1_projectai
streamlit run app.py
```

Enjoy your beautiful weather application! 🌤️⛅🌈

---

**For detailed help, see:**
- 📖 README.md - Full documentation
- ⚡ QUICKSTART.md - Quick reference
- 📊 PROJECT_SUMMARY.md - Complete overview
- 🔧 config.py - All customization options

**Version**: 1.0.0  
**Status**: ✅ Ready for Use  
**Last Updated**: November 14, 2025
