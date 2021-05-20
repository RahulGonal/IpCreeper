# Importing the modules
import ipinfo
import pprint
import time

print("Welcome to IP Creeper")
time.sleep(2)
print("The Creator of the tool is not responsible for any misuse of this tool")
time.sleep(2)
print("This tool is meant for educational purposes only")
time.sleep(3)
print("Ｉｐ Ｃｒｅｅｐｅｒ")
print("Created by Rahul.G")
time.sleep(5)
ip_address = input("Enter the IP Address of the victim >>>>> ")
time.sleep(2)
print("You need access token to continue, sign in to ipinfo.io to get access token")
time.sleep(3)
access_token = input("Enter the access token >>>>> ")
handler = ipinfo.getHandler(access_token)
details = handler.getDetails()
pprint.pprint(details.all)

print("Thank You for using the tool")
print("Subscribe to Rahul's youtube channel Rahul Rocks75")