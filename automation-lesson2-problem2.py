#!/usr/bin/env python

"""telnetlib

    a. Write a script that connects using telnet to the pynet-rtr1 router. Execute the 'show ip int brief' command on the router and return the output.

You should be able to do this by using the following items: 
"""

TELNET_PORT = 222
TELNET_TIMEOUT = 6

import telnetlib
#def main():
ip_addr = '184.105.247.70'
username =  'pyclass'
password = '88newclass'
remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
output = remote_conn.write(username + '\n')
output = remote_conn.read_until("sername:" ,TELNET_TIMEOUT)
print(output)
remote_conn.close()
"""remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
remote_conn.read_very_eager()
remote_conn.write(<command> + '\n')
remote_conn.close()
"""

