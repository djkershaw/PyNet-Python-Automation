#Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
import pexpect
import time
import sys
from getpass import getpass
ip_addr= '184.105.247.71'
username = 'pyclass'
port = 22
password =getpass()
ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username,ip_addr,port))
# ssh_conn.logfile =sys.stdout
ssh_conn.timeout = 3
ssh_conn.expect('ssword:')
ssh_conn.sendline(password)
ssh_conn.expect('#')
#ssh_conn.logfile = sys.stdout
ssh_conn.sendline('show ip int bri')
ssh_conn.expect('#')
print ssh_conn.before
