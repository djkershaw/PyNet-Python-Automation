"""8 Write a Python program using ciscoconfparse that parses this config file. 
Note, this config file is not fully valid (i.e. parts of the configuration are missing).
The script should find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO') 
and for each crypto map entry print out its children."""
from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
#print(dir(cisco_cfg))
crypto_lines = cisco_cfg.find_objects(r"crypto map CRYPTO")

match0 = crypto_lines[0]
for child in match0.children:
    print child.text

match1 = crypto_lines[1]
for child in match1.children:
    print child.text

match2 = crypto_lines[2]
for child in match2.children:
    print child.text

match3 = crypto_lines[3]
for child in match3.children:
    print child.text

match4 = crypto_lines[4]
for child in match4.children:
    print child.text



"""9. Find all of the crypto map entries that are using PFS group2"""
print("The matches for pfs group2 is")
print(cisco_cfg.find_objects(r"pfs group2"))




"""10. Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name). Print these entries and their corresponding transform set name."""
print("The lines without AES are")
print(cisco_cfg.find_objects_wo_child(parentspec=r"crypto map CRYPTO",childspec=r"AES"))

