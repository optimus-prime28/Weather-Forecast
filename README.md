#  Weather Forecast Pro

A professional, real-time weather forecasting web application built with **Streamlit** and **OpenWeatherMap API**. Get current weather conditions, 5-day forecasts, interactive charts, and detailed meteorological data for any city in the world.

##  Features

- **Real-Time Weather Data**: Current temperature, humidity, wind speed, pressure, and more
- **5-Day Forecast**: Interactive line charts for temperature trends and bar charts for humidity
- **Professional UI/UX**: Modern gradient design, responsive layout, custom styling
- **Weather Emojis**: Visual indicators for different weather conditions
- **Detailed Metrics**: Cloud cover, visibility, atmospheric pressure, wind direction
- **Data Caching**: 10-minute cache for improved performance and reduced API calls
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Error Handling**: User-friendly error messages and graceful API failure handling

##  Quick Start

### 1. Clone the Repository
git clone <your-repo-url>

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Set Up API Key
Create .streamlit/secrets.toml:
MY_API_KEY = "your_openweathermap_api_key"

### 4. Run the Application
streamlit run app.py

##  Tech Stack

- **Streamlit**: Web app framework
- **Plotly**: Interactive charts
- **Pandas**: Data processing
- **Requests**: HTTP client for APIs

##  Security

Never commit .streamlit/secrets.toml (contains API keys). The .gitignore file prevents this.

##  License

Open source - Free to use and modify.
