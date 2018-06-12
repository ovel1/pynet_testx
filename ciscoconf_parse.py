from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_configs/adelaide-r01.txt")
intf=cisco_cfg.find_objects(r"^interface")

for iface in intf:
    print(iface.text)    

