import numbers
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input("enter your number with area code")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
sim=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(sim)
print(reg)