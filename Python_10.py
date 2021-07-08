
from Python_8_3 import qytang_ping
from Python_9_1 import qytang_ssh
import re
import pprint


# ipadd_dict = {}
#
# for router_ip in list_ip:
#     ipadd_list = re.match(r'[\S\s]+([E|L]\S+[0-9])\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s+', router_ip).groups()
#     ipadd_dict[ipadd_list[0]] = (ipadd_list[1])
#
# print(ipadd_dict)



list_ip = "TCP outside Ethernet0/0:5223 inside 192.168.1.1:52419, idle 0:00:11, bytes 0, flags saA\n" \
            "TCP outside Ethernet0/1:80 dmz 10.1.1.1:57646, idle 0:00:29, bytes 2176, flags UIO\n" \
            "TCP outside Ethernet0/2:80 dmz 172.31.1.1:57646, idle 0:00:29, bytes 2176, flags UIO\n" \
            "TCP outside Loopback0:80 dmz 3.3.3.3:57646, idle 0:00:29, bytes 2176, flags UIO"

ipadd_dict = {}

for router_ip in list_ip.split('\n'):
    re_result = re.match(r'[\S\s]+\s+([E|L]\S+[0-9])\:[0-9]{1,5}\s+\w+\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\:([0-9]{1,5}).\s+\w+\s+\S+\,\s+bytes\s+(\d+),\s+\w+\s+(\w+)', router_ip).groups()
    ipadd_dict[re_result[0]] = (re_result[1])

print(ipadd_dict)

print('=' * 20)
pprint.pprint(ipadd_dict, indent=4)



ping_result = qytang_ping('192.168.32.1')

if ping_result:
    qytang_ssh('192.168.31.62', 'root', '!ningzhe305', cmd='show ip int brief')

else:
    print('ngngnng')












if __name__ == '__main__':
    pass
