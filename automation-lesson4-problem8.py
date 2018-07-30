'''Use Netmiko to change the logging buffer size (logging buffered <size>) and to 
disable console logging (no logging console) from a file on both pynet-rtr1 and 
pynet-rtr2 (see 'Errata and Other Info, item #4).'''

from netmiko import ConnectHandler

# Create dictionaries for the relavant network devices
rtr1 = { 'device_type':'cisco_ios','ip':'184.105.247.70','username':'pyclass',
'password':'88newclass'}
rtr2 = { 'device_type':'cisco_ios','ip':'184.105.247.71','username':'pyclass',
'password':'88newclass'}

# Open all connections
pynet_rtr1 = ConnectHandler(**rtr1)
pynet_rtr2 = ConnectHandler(**rtr2)

# Config the devices
pynet_rtr1.send_config_from_file(config_file='config_file.txt')
pynet_rtr2.send_config_from_file(config_file='config_file.txt')

# show the results
print('\n For rtr1 the result is\n')
output = pynet_rtr1.send_command('show run | include buffered')
print output

print('\n For rtr2the result is\n')
output = pynet_rtr2.send_command('show run | include buffered')
print output
