import ipinfo
from pprint import pprint
import time
from pyfiglet import figlet_format
from faker import Faker
import shodan

ascii_banner = figlet_format("IP CREEPER")
print(ascii_banner)

print("Created by RahulGonal")
time.sleep(5)
print("Welcome to IP Creeper")
time.sleep(5)
print("This tool is meant for educational purposes only")
time.sleep(5)

ip_address = input('Enter the IP Address of the victim >>>>> ')
print("You are going to need api keys of both Shodan and Ipinfo for Ip Info Gathering")
time.sleep(2)
ShoApi = str(input("Enter your shodan api key >>>> "))
shhh = shodan.Shodan(ShoApi)
Sinfo = shhh.host(ip_address)
IpApi = input('Type your access token or api key from ipinfo.io >>>>> ')
handler = ipinfo.getHandler(IpApi)
details = handler.getDetails(ip_address)
details.all
print("+++++++++++++++++++")
print("Results from Shodan")
print("+++++++++++++++++++")
pprint(Sinfo)
print('+++++++++++++++++++')
print("Results from IpInfo")
print("+++++++++++++++++++")
pprint(details.all)

pprint("Thank You for using my script")
pprint("                     Regards,")
pprint("                       -Rahul Gonal")
