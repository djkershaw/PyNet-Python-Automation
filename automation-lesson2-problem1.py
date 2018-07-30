"""Python Libraries 

    a. Make sure that you have PySNMP and Paramiko installed in the lab
 (i.e. enter the Python shell and test 'import pysnmp' and 'import 
paramiko')."""
import pysnmp
import paramiko


"""    b. Determine which version of PySNMP and Paramiko are installed.  
dir(pysnmp) and dir(paramiko) should be helpful here."""
print("pysnmp version is",pysnmp.version)
print("Paramiko version is",paramiko.__version_info__)
print("Here are the allowed paths for commands right now")
import sys
from pprint import pprint
pprint(sys.path)



"""    c. Write a simple Python module that contains one function that prints 'hello' (module name = my_func.py)."""


""" Do a test where you import my_func into a new Python script. Test this using the following contexts:
        * my_func.py is located in the same directory as your script"""
from function_library import my_func
my_func()

"""        * my_func.py is located in some random subdirectory (not the same directory as your script)"""
# From the OS execute the command export PYTHONPATH=/home/dkershaw/personal-library

"""* my_func.py is located in 'site-packages' of the virtual environment that you are using"""
