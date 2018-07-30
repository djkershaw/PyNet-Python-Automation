''' 1. Use Arista's eAPI to obtain 'show interfaces' from the switch. Parse the 'show interfaces' 
output to obtain the 'inOctets' and 'outOctets' fields for each of the interfaces on the switch.  Accomplish this using Arista's pyeapi.'''
import jsonrpclib
import ssl
import pyeapi
from pprint import pprint
ssl._create_default_https_context = ssl._create_unverified_context

ip_addr = '184.105.247.72' #(arista1.twb-tech.com)
ssh_port = '22'
eapi_port = '443'
username = 'pyclass'
password = '88newclass'
switch_url = 'https://{}:{}@{}:{}'.format(username, password, ip_addr, eapi_port)
#print(switch_url)
switch_url = switch_url + '/command-api'
#print('The full url is')
#print(switch_url)
#print(dir(jsonrpclib))
#print('\n\n\n')
#print(dir(jsonrpclib.Server))

remote_connect = jsonrpclib.Server(switch_url)
#print(dir(remote_connect))
output = remote_connect.runCmds(1,['show interfaces'])
some_dict = output[0]
interfaces =some_dict['interfaces']
#print(type(interfaces))
#pprint(interfaces)
#print('The keys are')
#print(interfaces.keys())

print('interface','input counters','output counters')

E1 = interfaces['Ethernet1']
E1counters = E1['interfaceCounters']
E1countersin= E1counters['inOctets']
E1countersout=E1counters['outOctets']
print('Ethernet1',E1countersin,E1countersout)  

E2 = interfaces['Ethernet2']
E2counters = E2['interfaceCounters']
E2countersin= E2counters['inOctets']
E2countersout=E2counters['outOctets']
print('Ethernet2',E2countersin,E2countersout)

E3 = interfaces['Ethernet3']
E3counters = E3['interfaceCounters']
E3countersin= E3counters['inOctets']
E3countersout=E3counters['outOctets']
print('Ethernet3',E3countersin,E3countersout)

E4 = interfaces['Ethernet4']
E4counters = E4['interfaceCounters']
E4countersin= E4counters['inOctets']
E4countersout=E4counters['outOctets']
print('Ethernet4',E4countersin,E4countersout)

E5 = interfaces['Ethernet5']
E5counters = E5['interfaceCounters']
E5countersin= E5counters['inOctets']
E5countersout=E5counters['outOctets']
print('Ethernet5',E5countersin,E5countersout)

E6 = interfaces['Ethernet6']
E6counters = E6['interfaceCounters']
E6countersin= E6counters['inOctets']
E6countersout=E6counters['outOctets']
print('Ethernet6',E6countersin,E6countersout)

E7 = interfaces['Ethernet7']
E7counters = E7['interfaceCounters']
E7countersin= E7counters['inOctets']
E7countersout=E7counters['outOctets']
print('Ethernet7',E7countersin,E7countersout)

