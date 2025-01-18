import argparse


USWFC_DESCRIPTION="United States Weather Forecast Utility"
COORDINATES_DESCRIPTION="Retrieve weather forecast associated with coordinates"


def main() -> None:
    parser = argparse.ArgumentParser(description=USWFC_DESCRIPTION)    
    parser.add_argument("-v", "--version", action="store_true", help="show uswfc version")
    subparsers = parser.add_subparsers(dest='command')

    # parse coordinates arguments
    parser_coordinates = subparsers.add_parser(
        "coordinates", 
        help=COORDINATES_DESCRIPTION, 
        description=COORDINATES_DESCRIPTION
    )
    parser_coordinates.add_argument("latitude", type=float, metavar="LATITUDE", help="Latitude coordinate")
    parser_coordinates.add_argument("longitude", type=float, metavar="LONGITUDE", help="Longitude coordinate")
    arguments = parser.parse_args()

    if arguments.version:
        from . import __version__
        print(f"uswfc {__version__}")        
