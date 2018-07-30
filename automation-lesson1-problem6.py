"""Write a Python program that creates a list. One of the elements of the list should be a dictionary with at least two keys."""
import yaml
import json

print("This is a test")
MyList =["list_element1","list_element2"]
bgp_fields ={'bgp_as':'1','peer_as':'2','peer_ip':'10.10.10.10'}
MyList.append(bgp_fields)
print(type(MyList))

  
"""Write this list out to a file using both YAML and JSON formats. The YAML file should be in the expanded form."""
print(yaml.dump(MyList, default_flow_style = False))
with open("a_file.yml","w") as f:
 f.write(yaml.dump(MyList, default_flow_style = False))

print(json.dumps(MyList))
with open("a_file.json","w") as f:
    json.dump(MyList,f)

