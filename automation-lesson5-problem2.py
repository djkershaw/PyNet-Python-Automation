#!/usr/bin/env python
'''Using Arista's pyeapi, create a script that allows you to add a VLAN (both the VLAN ID and the VLAN name).  

Your script should first check that the VLAN ID is available and only add the VLAN if it doesn't already exist.  Use VLAN IDs between 100 and 999.  You should be able to call the script from the command line as follows:

   python eapi_vlan.py --name blue 100     # add VLAN100, name blue

If you call the script with the --remove option, the VLAN will be removed.

   python eapi_vlan.py --remove 100          # remove VLAN100

Once again only remove the VLAN if it exists on the switch.  You will probably want to use Python's argparse to accomplish the argument processing.

In the lab environment, if you want to directly execute your script, then you will need to use '#!/usr/bin/env python' at the top of the script (instead of '!#/usr/bin/python').'''

import argparse
import pyeapi
import jsonrpclib
import ssl
from pprint import pprint
ssl._create_default_https_context = ssl._create_unverified_context

# parse the input arguements
parser = argparse.ArgumentParser()
args = parser.parse_args()
print type(args)



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
#pprint(output)

commands =[] # initialize list
commands.append('vlan 226')
commands.insert(0,'configure terminal')
commands.insert(0, {'cmd': 'enable', 'input':''}) 
commands.append('name orange')
#print(commands)
remote_connect.runCmds(1, commands)

