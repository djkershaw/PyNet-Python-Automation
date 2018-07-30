# Use Pexpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2. Verify this change by examining the output of 'show run'.
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
ssh_conn.sendline('config t')
#print ssh_conn.after
ssh_conn.expect('pynet')
ssh_conn.logfile = sys.stdout
#print ssh_conn.after
ssh_conn.sendline('logging buffered 32768')
ssh_conn.expect('pynet')
#sys_conn.sendline('exit')
#sys_conn.expect('#')
ssh_conn.sendline('show run | inc buffered')
ssh_conn.expect('#')
print ssh_conn.after

