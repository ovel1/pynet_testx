ip_addr1="192.168.1.1"
ip_addr2="10.1.1.1"
ip_addr3="172.16.1.1"

print ("\n")
print ("-" * 80)

print ("{my_ip:^20}{ip:^20}{ip_alt:^20}".format(ip_alt=ip_addr1, ip=ip_addr2, my_ip=ip_addr3))

print ("-" * 80)
print ("\n")

octets = ip_addr1.split('.')
