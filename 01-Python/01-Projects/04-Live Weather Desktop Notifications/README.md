# Weather Notification Script

A simple Python script that fetches current weather data for a specified city and displays a desktop notification with temperature and wind speed information.

## Features

- Retrieves geographic coordinates for any city using the Open-Meteo Geocoding API
- Fetches real-time weather data including temperature and wind speed
- Displays cross-platform desktop notifications
- Lightweight with minimal dependencies

## Prerequisites

- Python 3.6 or higher
- Internet connection

## Installation

1. Clone or download this script to your local machine

2. Install the required dependencies:

```bash
pip install requests plyer
```

## Dependencies

- **requests**: For making HTTP requests to the weather APIs
- **plyer**: For cross-platform desktop notifications

## Usage

1. Open the script and modify the `city` variable to your desired location:

```python
city = "Cairo"  # Change to your city
```

2. Run the script:

```bash
python weather_notification.py
```

3. The script will:
   - Print the weather information to the console
   - Display a desktop notification with the current weather

## Example Output

**Console:**
```
Weather: Cairo: 22.5°C, Wind 15 km/h
```

**Notification:**
- Title: "Weather Update"
- Message: "Cairo: 22.5°C, Wind 15 km/h"

## How It Works

1. **Geocoding**: Converts the city name to latitude and longitude coordinates using the Open-Meteo Geocoding API
2. **Weather Data**: Retrieves current weather information using the Open-Meteo Forecast API
3. **Notification**: Displays a system notification with the weather details

## API Information

This script uses free APIs from [Open-Meteo](https://open-meteo.com/):
- Geocoding API: No authentication required
- Weather API: No authentication required

## Troubleshooting

**City not found:**
- Verify the city name spelling
- Try using the full city name or including country information

**Notification not appearing:**
- Ensure notification permissions are enabled on your system
- On Linux, you may need to install additional notification packages (e.g., `libnotify`)

**Module not found errors:**
- Run `pip install requests plyer` to install dependencies

## Customization

You can modify the script to:
- Add more weather parameters (humidity, precipitation, etc.)
- Change notification duration by adjusting the `timeout` parameter
- Schedule the script to run periodically using cron (Linux/Mac) or Task Scheduler (Windows)

## License

This script is provided as-is for educational and personal use.

## Contributing

Feel free to fork and enhance this script with additional features such as:
- Multiple city support
- Weather alerts
- Historical data tracking
- GUI interface