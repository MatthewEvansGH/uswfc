import argparse
from . import weather


USWFC_DESCRIPTION="United States Weather Forecast Utility"
COORDINATES_DESCRIPTION="Retrieve weather forecast associated with coordinates"


def _parse_arguments() -> argparse.Namespace:
    """ Parses uswfc arguments. """
    parser = argparse.ArgumentParser(description=USWFC_DESCRIPTION)    
    parser.add_argument("-v", "--version", action="store_true", help="show uswfc version")
    subparsers = parser.add_subparsers(dest='command')

    # parse coordinates arguments
    parser_coordinates = subparsers.add_parser("coordinates", help=COORDINATES_DESCRIPTION, 
                                               description=COORDINATES_DESCRIPTION)
    parser_coordinates.add_argument("latitude", type=float, metavar="LATITUDE", help="Latitude coordinate")
    parser_coordinates.add_argument("longitude", type=float, metavar="LONGITUDE", help="Longitude coordinate")
    return parser.parse_args() 


def _fetch_coordinates_forecast(arguments: argparse.Namespace) -> None:
    """ Retrieves and prints forecast data for coordinates. """
    forecast_data = weather.fetch_forecast(arguments.latitude, arguments.longitude)
    print(f"\nWeather Forecast for {forecast_data["location"]}\n")
    for forecast in forecast_data["periods"]:
        print(f"[{forecast["name"]}, {forecast["day"]}]")
        print(forecast["forecast"])
        print(f"Temperature: {forecast["temperature"]}")
        print(f"Wind: {forecast["wind"]}")
        print(f"Precipitation: {forecast["precipitation"]}\n")


def main() -> None:
    """ Entry point for uswfc utility. """
    arguments = _parse_arguments()
    if arguments.version:
        from . import __version__
        print(f"uswfc {__version__}")        
    if arguments.command == "coordinates":
        _fetch_coordinates_forecast(arguments)