# This code will give you the location of mobile and it's information according to mobile number.
# import modules:
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

phone_number = phonenumbers.parse("+91**********") #Here you enter the phone number of which you want to know the location along with the country code.

print(geocoder.description_for_number(phone_number,'en')) # This line of code will give you location
print(carrier.name_for_number(phone_number, 'en')) # This line of code will give you SIM type.

