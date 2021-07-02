import ipinfo
from pprint import pprint
import time
from pyfiglet import figlet_format
from random import randint
from colorama import Fore,Style
from faker import Faker
import shodan

font = ['slant', "3-d", "3x5", "5lineoblique",
        "alphabet", "banner3-D", "doh", "isometric1", "letters",
        "alligator", "dotmatrix", "bubble", "bulbhead", "digital"]
random_choice = randint(0, len(font))
ascii_art = figlet_format("IpCreeper", font=font[random_choice])
print(Fore.GREEN + ascii_art)
print(Style.RESET_ALL)

print("Created by RahulGonal")
time.sleep(5)
print("Welcome to IP Creeper")
time.sleep(5)
print("This tool is meant for educational purposes only")
time.sleep(5)

ip_address = input('Enter the IP Address of the victim >>>>> ')

print("There are two ways to get the information but both need api keys.")
print("So Go to their Respective websites below and sign in to get api key.")
time.sleep(3)
print("1.Shodan (https://www.shodan.io)")
print("2.IpInfo (https://ipinfo.io")
print('3.Both (You will need both the websites api keys for this)')
Website = input("Choose One Option >>>> ")

if "1" or "Shodan" in Website:
    sApi = input("Enter your shodan api key >>>> ")
    Sipinfo = sApi.host(ip_address)
    print(Sipinfo)

if "2" or "IpInfo" in Website:
    access_token = input('Type your access token or api key from ipinfo.io >>>>> ')
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    details.all
    pprint(details.all)

if "3" or "Both" in Website:
    ShApi = input("Enter your shodan api key >>>> ")
    Sinfo = sApi.host(ip_address)
    IpApi = input('Type your access token or api key from ipinfo.io >>>>> ')
    handler = ipinfo.getHandler(IpApi)
    details = handler.getDetails(ip_address)
    details.all
    print("Results from Shodan")
    pprint(Sinfo)
    print("Results from IpInfo")
    pprint(details.all)
    
    
print("Thank You for using the tool")
print("Subscribe to Rahul's youtube channel Rahul Rocks75")
