# uswfc
A simple United States weather forecast utility (uswfc) to explore developing a Python package, 
CI/CD pipelines, and GitHub features.

## Usage
The `uswfc` command-line utility is cross-platform and can be used in terminals on Windows, Linux, and macOS.
```sh
uswfc [-h] [-v]
```
**Options:**
- `-h, --help` show uwfwc help information
- `-v, --version` show uswfc version

### coordinates

Retrieve weather forecast associated with (latitude, longitude) coordinates.
```sh
uswfc coordinates [-h] LATITUDE LONGITUDE
```
**Postional Arguments:**
- `LATITUDE` latitude coordinate
- `LONGITUDE` longitude coordinate

**Options:**
- `-h, --help` show usfwc coordinates help information

## Resources
[National Weather Server API](https://www.weather.gov/documentation/services-web-api#/default/point)