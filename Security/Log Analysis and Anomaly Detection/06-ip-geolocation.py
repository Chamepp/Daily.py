import geoip2.database

def geolocate_ip(ip_address):
    # Path to the GeoIP database file
    database_file = 'GeoLite2-City.mmdb'

    try:
        # Load the GeoIP database
        reader = geoip2.database.Reader(database_file)

        # Perform IP geolocation lookup
        response = reader.city(ip_address)

        # Extract relevant information
        country = response.country.name
        city = response.city.name
        latitude = response.location.latitude
        longitude = response.location.longitude

        # Print geolocation information
        print(f"IP Address: {ip_address}")
        print(f"Country: {country}")
        print(f"City: {city}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")

    except geoip2.errors.AddressNotFoundError:
        print(f"No geolocation data found for IP address: {ip_address}")

    finally:
        # Close the GeoIP database reader
        reader.close()

# Example usage
ip_address = input("Enter an IP address for geolocation: ")
geolocate_ip(ip_address)

