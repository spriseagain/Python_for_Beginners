#Taking input from user and displaying the result

# importing translator library from googletrnas
from googletrans import Translator

translator = Translator()

from geopy.geocoders import Nominatim
# Create a geolocator object
geolocator = Nominatim(user_agent="geoapiExercises")

# Latitude and Longitude
latitude = float(input("Enter the Latitude"))
longitude = float(input("Enter the Longitude"))

# Get the location
location = geolocator.reverse((latitude, longitude))
loc = location.address

translated = translator.translate(loc, dest='en')

print(translated.text)

