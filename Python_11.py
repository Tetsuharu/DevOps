
from Python_9_1 import qytang_ssh
import re
import hashlib
import time


def qytang_get_config(ip, username='admin', password='Cisc0123'):
    try:
        hostname_config = qytang_ssh(ip, 'admin', 'Cisc0123', cmd='show run | begin hostname')
        hostname_device = re.match(r'[\s\S]+hostname\s+(\S+)\s+', hostname_config).groups()
        m = hashlib.md5()
        m.update(hostname_device[0].encode())
        return m.hexdigest()
    except Exception:
        return


def qytang_check_diff(ip, username='admin', password='Cisc0123'):
    beforce_md5 = ''
    while True:
        device_md5 = qytang_get_config(ip)
        first_md5 = beforce_md5.replace('', device_md5)
        if first_md5 == device_md5:
            while True:
                after_md5 = qytang_get_config(ip)
                if after_md5 == first_md5:
                    print(first_md5)
                else:
                    print(after_md5)
                    print('MD5 value changed')
                    break
                time.sleep(5)
            break
        time.sleep(5)




if __name__ == '__main__':
    # print(qytang_get_config('192.168.31.200', username='admin', password='Cisc0123'))
    qytang_check_diff('192.168.31.200', username='admin', password='Cisc0123')

