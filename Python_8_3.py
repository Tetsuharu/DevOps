
import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)

from kamene.all import *

def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip + " 通！"
    else:
        return ip + " 不通！"

if __name__ == '__main__':
    result = qytang_ping('183.79.102.200')
    if result:
        print(str(result))
    else:
        print(str(result))

