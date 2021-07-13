
from Python_8_3 import qytang_ping
from Python_9_1 import qytang_ssh
import re
import pprint


def qytang_get_if(*ips, username='admin', password='Cisc0123'):
    device_if_dict = {}
    ipadd_dict = {}
    ping_list = [*ips]
    for p in ping_list:
        plist = qytang_ping(p)
        if plist:
            rlist = qytang_ssh(p, 'admin', 'Cisc0123', cmd='show ip int b')
            ilist = re.findall(r'([G|L]\S+[0-9])\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s+', rlist)
            for x in ilist:
                ipadd_dict[x[0]] = (x[1])
            device_if_dict[p] = (ipadd_dict)
        else:
            ipadd_dict = {}
            device_if_dict[p] = (ipadd_dict)
    return device_if_dict


if __name__ == '__main__':
    pprint.pprint(qytang_get_if('192.168.31.200', '192.168.31.201', username='admin', password='Cisc0123'), indent=4)











if __name__ == '__main__':
    pass
