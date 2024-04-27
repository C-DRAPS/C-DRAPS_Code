# TODO: This is a replacement for Google's Geocoding API (free). It takes a single address -> tries to
#  convert it to it's full address -> gets and returns coordinates.
#  Program handles TimeoutErrors. Program prints it's own status updates.
import time
from geopy.geocoders import Nominatim


def getCoordinates(address):
    status = "failed"

    while status == "failed":
        try:
            # Initialize the geocoder
            geolocator = Nominatim(user_agent="geocoding_app")

            # Perform geocoding
            location = geolocator.geocode(address, timeout=120)

            # Return values
            print(f"\n{address}  ==>  {location}")
            if location:
                print("Latitude:", location.latitude)
                print("Longitude:", location.longitude)
                status = "passed"
                return location.latitude, location.longitude
            else:
                print("Location not found")
                status = "passed"
                return -1, -1

        except TimeoutError:
            print("@@@ SYSTEM TIMEOUT @@@   |   sleep for 60 sec...")
            time.sleep(60)
