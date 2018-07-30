#Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2.
import paramiko
import time
# paramiko is python ssh library
from getpass import getpass
ip_addr= '184.105.247.70'
username = 'pyclass'
port = 22
password =getpass()
remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip_addr,username=username,password=password,look_for_keys=False, allow_agent=False,port=port)
remote_conn = remote_conn_pre.invoke_shell()
time.sleep(1)
#clear_buffer(remote_conn)
#output = remote_conn.recv(5000)
#print (output)
remote_conn.send("show version\n")
time.sleep(1)
output = remote_conn.recv(5000)
print output
