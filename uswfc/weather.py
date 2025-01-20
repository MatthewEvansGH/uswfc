import requests
from datetime import datetime


def fetch_forecast(latitude: float, longitude: float) -> dict[str, any]:
    """ Fetches forecast from the National Weather Service API. """
    
    def _parse_period(data: dict[str, any]) -> dict[str, any]:
        """ Parses individual forecast period from NWS API. """
        try:
            day = datetime.fromisoformat(data["startTime"]).strftime("%B %d, %Y")
            precipitation = f"{data["probabilityOfPrecipitation"]["value"]}%"
            if not data["probabilityOfPrecipitation"]["value"]:
                precipitation = "N/A"
            return {
                "name": data["name"],
                "day": day,
                "forecast": data["shortForecast"],
                "temperature": f"{data["temperature"]}{data["temperatureUnit"]}",
                "wind": f"{data["windSpeed"]} {data["windDirection"]}",
                "precipitation": precipitation
            }
        except ValueError:
            print("Error: Non-ISO date format fetched from forecast API")
            exit(1)
        
    try:
        # Fetch initial points data using coordinates.
        points_data = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}").json()
        city = points_data["properties"]["relativeLocation"]["properties"]["city"]
        state = points_data["properties"]["relativeLocation"]["properties"]["state"]

        # Fetch forecast data
        forecast = { "location": f"{city}, {state}", "periods": [] }
        forecast_data = requests.get(points_data["properties"]["forecast"]).json()
        for period in forecast_data["properties"]["periods"]:
            forecast["periods"].append(_parse_period(period))
        return forecast
    except requests.exceptions.JSONDecodeError as e:
        print("Error: Invalid JSON fetched from forecast API")
        exit(e.errno)
    except KeyError as e:
        print("Error: Unexpected data format fetched from forecast API")
        exit(1)
    except requests.exceptions.RequestException as e:
        print("Error: Something went wrong requesting the forecast API")
        exit(e.errno)