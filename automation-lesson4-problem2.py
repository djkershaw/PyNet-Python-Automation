#Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2. This will require that you enter into configuration mode.

import paramiko
import time
# paramiko is python ssh library
from getpass import getpass
ip_addr= '184.105.247.70'
username = 'pyclass'
port = 22
password =getpass()
remote_conn_pre = paramiko.SSHClient()
#remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.load_system_host_keys()
remote_conn_pre.connect(ip_addr,username=username,password=password,look_for_keys=False, allow_agent=False,port=port)
remote_conn = remote_conn_pre.invoke_shell()
time.sleep(1)
#clear_buffer(remote_conn)
#output = remote_conn.recv(5000)
#print (output)
remote_conn.send("config t\n")
time.sleep(1)
remote_conn.send("logging buffered 32768\n")
time.sleep(1)
#output = remote_conn.recv(5000)
#print output
remote_conn.send("exit\n")
time.sleep(1)
remote_conn.send("show run | include buffer\n")
time.sleep(1)
output = remote_conn.recv(5000)
print output
