import unittest
from unittest.mock import patch, MagicMock


class TestWeather(unittest.TestCase):
    @patch('uswfc.weather.requests.get')
    def test_fetch_forecast_successful(self, mock_get):
        mock_points_data = {
            "properties": {
                "relativeLocation": {
                    "properties": {
                        "city": "Los Angeles",
                        "state": "CA"
                    }
                },
                "forecast": "http://mock-forecast-url"
            }
        }
        mock_forecast_data = {
            "properties": {
                "periods": [{"startTime": "2025-01-19T00:00:00-08:00", "name": "Today", "shortForecast": "Rain", 
                             "temperature": 75, "temperatureUnit": "F", "windSpeed": "5 mph", "windDirection": "NE", 
                             "probabilityOfPrecipitation": {"value": 100}}]
            }
        }
        mock_get.side_effect = [
            MagicMock(json=MagicMock(return_value=mock_points_data)),
            MagicMock(json=MagicMock(return_value=mock_forecast_data))
        ]
        
        from uswfc.weather import fetch_forecast
        forecast = fetch_forecast(34.0522, -118.2437)
        
        self.assertEqual(forecast["location"], "Los Angeles, CA")
        self.assertEqual(len(forecast["periods"]), 1)
        self.assertEqual(forecast["periods"][0]["name"], "Today")
        self.assertEqual(forecast["periods"][0]["forecast"], "Rain")
        self.assertEqual(forecast["periods"][0]["temperature"], "75F")
        self.assertEqual(forecast["periods"][0]["wind"], "5 mph NE")
        self.assertEqual(forecast["periods"][0]["precipitation"], "100%")
