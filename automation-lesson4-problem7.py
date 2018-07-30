#Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2.

from netmiko import ConnectHandler

# Create dictionaries for the relavant network devices


rtr2 = { 'device_type':'cisco_ios','ip':'184.105.247.71','username':'pyclass',
'password':'88newclass'}


# Open all connections
pynet_rtr2 = ConnectHandler(**rtr2)

config_commands = ['config t','logging buffered 16384','exit',]
pynet_rtr2.send_config_set(config_commands)
output = pynet_rtr2.send_command('show run | include buffered')
print output
