import phonenumbers
import opencage
import folium
from phonenumbers import geocoder

number=input("Enter phone number : ")

# Parse the phone number
pepnumber = phonenumbers.parse(number)

# Get the location description for the phone number
location = geocoder.description_for_number(pepnumber, 'en')

print(location)
from phonenumbers import carrier
service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro , "en" ))

from opencage.geocoder import OpenCageGeocode
key="ccad45bcf49f4a4fb3425eedb5f3e288"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)
myMap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup = location).add_to(myMap)
myMap.save("mylocation.html")