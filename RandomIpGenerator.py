from faker import Faker 
faker = Faker()
ip_addr = faker.ipv4()  
print(ip_addr)