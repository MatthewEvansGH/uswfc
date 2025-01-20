import sys
import unittest
import argparse
from unittest.mock import patch


class TestVersion(unittest.TestCase):
    @patch("builtins.print")
    def test_version_argument(self, mock_print):
        test_args = ["uswfc", "--version"]
        with patch.object(sys, 'argv', test_args):
            from uswfc.cli import main
            with patch("uswfc.__version__", "1.0.0"):
                main()
                mock_print.assert_called_with("uswfc 1.0.0")
                

class TestCoordinates(unittest.TestCase):
    @patch('uswfc.cli.weather.fetch_forecast')
    @patch('builtins.print')
    def test_fetch_coordinates_forecast_successful(self, mock_print, mock_fetch_forecast):
        arguments = argparse.Namespace(latitude=34.0522, longitude=-118.2437)
        mock_fetch_forecast.return_value = {
            "location": "Los Angeles, CA",
            "periods": [{"name": "Today",  "day": "January 19, 2025", "forecast": "Rain", "temperature": "75F", 
                         "wind": "5 mph NE", "precipitation": "100%"}]
        }

        from uswfc.cli import _fetch_coordinates_forecast
        _fetch_coordinates_forecast(arguments)
        
        mock_print.assert_any_call("\nWeather Forecast for Los Angeles, CA\n")
        mock_print.assert_any_call("[Today, January 19, 2025]")
        mock_print.assert_any_call("Rain")
        mock_print.assert_any_call("Temperature: 75F")
        mock_print.assert_any_call("Wind: 5 mph NE")
        mock_print.assert_any_call("Precipitation: 100%\n")
