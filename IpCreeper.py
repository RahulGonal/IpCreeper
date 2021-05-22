import ipinfo
from pprint import pprint
import time

print("Ｉｐ Ｃｒｅｅｐｅｒ")
print("Created by RahulGonal")
time.sleep(5)
print("Welcome to IP Creeper")
time.sleep(5)
print("The Creator of the tool is not responsible for any misuse of this tool")
time.sleep(5)
print("This tool is meant for educational purposes only")
time.sleep(5)


print("You need access token to continue, sign in to ipinfo.io to get access token")
time.sleep(5)
access_token = input('Type your access token from ipinfo.io >>>>> ')
handler = ipinfo.getHandler(access_token)
ip_address = input('Enter the IP Address of the victim >>>>> ')
details = handler.getDetails(ip_address)
details.all
pprint(details.all)

print("Thank You for using the tool")
print("Subscribe to Rahul's youtube channel Rahul Rocks75")
