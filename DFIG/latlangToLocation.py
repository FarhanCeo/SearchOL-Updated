# import module
from geopy.geocoders import Nominatim
"""
# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")
# Latitude & Longitude input
Latitude = "26.201975"
Longitude = "78.1405861111111"

location = geolocator.reverse(Latitude+","+Longitude)

# Display
print(location)
address = location.raw['address']
print(address)
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
code = address.get('country_code')
zipcode = address.get('postcode')
print('City : ',city)
print('State : ',state)
print('Country : ',country)
print('Zip Code : ', zipcode)
"""


def get_location_name(lat, lon):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(lat+","+lon)
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    code = address.get('country_code')
    zipcode = address.get('postcode')
    return city, state, country, code, zipcode