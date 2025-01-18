import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Weather Forecast API Utility")    
    parser.add_argument("-v", "--version", action="store_true", help="show weatherf version")
    arguments = parser.parse_args()

    if arguments.version:
        from . import __version__
        print(f"uswfc {__version__}")