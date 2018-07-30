# Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to verify your state (i.e. that you are currently in configuration mode).
from netmiko import ConnectHandler
from getpass import getpass
rtr2 = { 'device_type':'cisco_ios','ip':'184.105.247.71','username':'pyclass',
'password':'88newclass'}
pynet_rtr2 = ConnectHandler(**rtr2)
pynet_rtr2.config_mode()
print ('Are we in config mode for pynet_rtr2?')
print (pynet_rtr2.check_config_mode())

