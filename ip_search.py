# Script to prompt the user for an IPv4 address and run
# it through a series of checks to determine its class and other attributes 

import ipaddress
#prompt user to enter IPv4
ip=input("Enter IPv4 Here [in CIDR notation] >")

#checks to take imputted IP and determine class
if ipaddress.ip_network(ip).is_multicast==True:
	print(f"The address {ip} is reserved for multicast use.")
elif ipaddress.ip_network(ip).is_private==True:
	print(f"The address {ip} is allocated for private networks.")
elif ipaddress.ip_network(ip).is_global==True:
	print(f"The address {ip} is allocated for public networks.")
elif ipaddress.ip_network(ip).is_reserved==True:
	print(f"The address {ip} is part of an IETF reserved block.")
elif ipaddress.ip_network(ip).is_loopback==True:
	print(f"The address {ip} is a loopback address.")
elif ipaddress.ip_network(ip).is_link_local==True:
	print(f"The address {ip} is reserved for link-local usage.")
elif ipaddress.ip_network(ip).is_unspecified==True:
	print(f"The address {ip} is of unspecified use.")
else: 
	print(f"The address {ip} is not able to be categorized.")

#converts imputed ip into a new varible to display net and host masks
net1=ipaddress.ip_network(ip)
print(f"The netmask for this IP is: {net1.netmask} ")
print(f"The hostmask for this IP is: {net1.hostmask} ")