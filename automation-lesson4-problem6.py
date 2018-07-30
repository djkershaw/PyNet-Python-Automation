# Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
from netmiko import ConnectHandler

# Create dictionaries for the relavant network devices

rtr1 = { 'device_type':'cisco_ios','ip':'184.105.247.70','username':'pyclass',
'password':'88newclass'}

rtr2 = { 'device_type':'cisco_ios','ip':'184.105.247.71','username':'pyclass',
'password':'88newclass'}

srx = { 'device_type':'juniper','ip':'184.105.247.76','username':'pyclass',
'password':'88newclass','secret':'','port':'22'}

# Open all connections
pynet_rtr1 = ConnectHandler(**rtr1)
pynet_rtr2 = ConnectHandler(**rtr2)
pynet_srx = ConnectHandler(**srx)

output = pynet_rtr1.send_command("show arp")
print("\nFor pynet_rtr1 we have arp")
print output
print ('\n')

output = pynet_rtr2.send_command("show arp")
print("For pynet_rtr2 we have arp")
print output
print ('\n')

output = pynet_srx.send_command("show arp")
print("For pynet_rtr2 we have arp")
print output
print ('\n')

