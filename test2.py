from test_ping import qytang_ping
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
list_ips = ('1.1.1.1', '1.1.3.3')

def qytang_get_if(*ips, username='admin', password='Cisco123'):
    device_if_dict = {}
    for x in list_ips:
        xlist = qytang_ping(x)
        ip_xxx = {}
        if xlist:
            for router_ip in list_ip.split('\n'):
                re_result = re.match(
                    r'[\S\s]+\s+([E|L]\S+[0-9])\:[0-9]{1,5}\s+\w+\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\:([0-9]{1,5}).\s+\w+\s+\S+\,\s+bytes\s+(\d+),\s+\w+\s+(\w+)',
                    router_ip).groups()
                ip_xxx[re_result[0]] = (re_result[1])
        else:
            return ''
        device_if_dict[x]=(ip_xxx)
    return device_if_dict

xxxx = qytang_get_if('1.1.1.1', username='admin', password='Cisco123')
pprint.pprint(xxxx, indent=4)


# ping_result = qytang_ping('1.1.1.1')
# if ping_result:
#     ipadd_dict = {}
#     for router_ip in list_ip.split('\n'):
#          re_result = re.match(
#              r'[\S\s]+\s+([E|L]\S+[0-9])\:[0-9]{1,5}\s+\w+\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\:([0-9]{1,5}).\s+\w+\s+\S+\,\s+bytes\s+(\d+),\s+\w+\s+(\w+)',
#              router_ip).groups()
#          ipadd_dict[re_result[0]] = (re_result[1])
#     pprint.pprint(ipadd_dict, indent=4)
# else:
#     print('ngngnng')






