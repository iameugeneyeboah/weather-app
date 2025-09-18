## Weather Reporter CLI

This project is a simple command-line weather reporter that fetches and presents the latest weather updates for any city using the OpenWeatherMap API via the `pyowm` Python library.

### Features
- Fetches current weather for any city and country
- Displays temperature, humidity, wind speed, and weather status
- User-friendly, formatted weather report

### Requirements
Install dependencies with:

```bash
pip install -r requirements.txt
```

### Usage
Run the script in your terminal:

```bash
python weather2.py
```

You will be prompted to enter:
- City name (e.g., Accra)
- Country code (e.g., GH for Ghana, US for USA)

Example output:
```
Good day, this is Eugene Yeboah, reporting live from Radio Universe, Legon.
Here's the latest weather update for Accra, GH:
Currently, we are experiencing clear sky with a temperature of 28°C (feels like 30°C). Humidity is at 70%, and wind speeds are around 3 m/s.
Stay tuned to CNN for more updates.
you can follow me on social media at theturksonphotography
```

### Configuration
The script uses a hardcoded OpenWeatherMap API key. For production use, consider storing your API key securely (e.g., in environment variables).

### Author
Eugene Yeboah

### License
This project is for educational and personal use.

### Contributing
Contributions are welcome! To contribute:
- Fork the repository
- Create a new branch for your feature or bugfix
- Make your changes and add tests if applicable
- Submit a pull request with a clear description of your changes

For major changes, please open an issue first to discuss what you would like to change.
