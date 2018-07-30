"""Write a Python program that reads both the YAML file and the JSON file created in exercise6 and pretty prints the data structure that is returned."""
import json
import yaml

with open("a_file.json") as f:
    json_file = json.load(f)
#print(json_file)

print("Here we print the json file")

from pprint import pprint as pp
pp(json_file)

#print("Now we print the yml file")

with open("a_file.yml") as f:
    yml_file = yaml.load(f)
pp(yml_file)
