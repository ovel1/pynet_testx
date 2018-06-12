from ciscoconfparse import CiscoConfParse
from pprint import pprint as pp
import yaml
import json

cisco_cfg = CiscoConfParse("cisco_configs/adelaide-r01.txt")
intf=cisco_cfg.find_objects(r"^interface")

for iface in intf:
    print(iface.text)    
# from the lab

mylist=list(range(8))
mylist.append('string1')
mylist.append('string2')
mylist.append(7)
mylist.append(10)
mylist.append({})
mylist[-1]['keys']='values'
mylist[-1]['ip_addr']='192.168.1.1'


with open("output-files/output.yaml", "w") as f:
    f.write(yaml.dump(mylist,default_flow_style=False))

with open("output-files/output.yaml") as f:
    new_mylist=yaml.load(f)

print("New list:")
print(yaml.dump(new_mylist, default_flow_style=False))

with open("output-files/output.txt", "w") as f:
    json.dump(mylist, f)

print("Json stuff")

with open("output-files/output.txt") as f:
    new_json_list = json.load(f)

pp(new_json_list)
