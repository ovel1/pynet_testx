from ciscoconfparse import CiscoConfParse
from pprint import pprint as pp
import yaml
import json

cisco_cfg = CiscoConfParse("cisco_configs/pynet-cisco-conf.txt")
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

print("New YAML list from file :")
print(yaml.dump(new_mylist, default_flow_style=False))

with open("output-files/output.txt", "w") as f:
    json.dump(mylist, f)

with open("output-files/output.txt") as f:
    new_json_list = json.load(f)

print("Json stuff from file:")
pp(new_json_list)

pfs_crypto=list()
nonaes_crypto=list()
crypto_maps=cisco_cfg.find_objects(r"^crypto map CRYPTO")

for cryptomap in crypto_maps:
    if cryptomap.re_search_children(r"set pfs group2"):
        pfs_crypto.append(cryptomap)
    if not cryptomap.re_search_children(r"AES-SHA"):
        nonaes_crypto.append(cryptomap)

print("PFS group2 crypto maps:")
for printobj in pfs_crypto:
    print(printobj.text)

print("Non AES crypto maps:")
for printobj in nonaes_crypto:
    print(printobj.text)

