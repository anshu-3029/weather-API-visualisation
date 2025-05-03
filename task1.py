import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

API_KEY = '9f3e8f64723f4cff960d6c1d0a755877'  # Replace with your real API key
CITY_NAME = 'Singapore'
API_URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY_NAME}&appid={API_KEY}&units=metric'

response = requests.get(API_URL)
weather_data = response.json()

# Check if the API returned data successfully
if response.status_code != 200:
    print("❌ Error fetching data:", weather_data.get("message", "Unknown error"))
    exit()

# Check if 'list' is in the response
if 'list' not in weather_data:
    print("❌ 'list' key not found in API response.")
    print("Raw response:", weather_data)
    exit()

# Extract and process data
timestamps = []
temperatures = []
humidities = []

for item in weather_data['list']:
    timestamps.append(datetime.datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S'))
    temperatures.append(item['main']['temp'])
    humidities.append(item['main']['humidity'])

# === PLOT DASHBOARD ===
sns.set(style='darkgrid')
plt.figure(figsize=(16, 6))

# Temperature Line Plot
plt.subplot(1, 2, 1)
sns.lineplot(x=timestamps, y=temperatures, marker='o', color='orangered')
plt.title(f'Temperature Forecast for {CITY_NAME}')
plt.xlabel('Date/Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)

# Humidity Bar Plot
plt.subplot(1, 2, 2)
sns.barplot(x=timestamps[:10], y=humidities[:10], palette='Blues_d')
plt.title(f'Humidity Forecast for {CITY_NAME} (First 10 Timestamps)')
plt.xlabel('Date/Time')
plt.ylabel('Humidity (%)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
