import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

class QYTPING:
    def __init__(self, ip, srcip=None, length=100):
        self.ip = ip
        self.srcip = srcip
        self.length = length
        self.ping_ip = IP(src=self.srcip, dst=self.ip) / ICMP() / (b'x'*self.length)

    def one(self):
        self.ping_ip = IP(src=self.srcip, dst=self.ip) / ICMP() / (b'x' * self.length)
        self.ping_result = sr1(self.ping_ip, timeout=2, verbose=False)
        if self.ping_result:
            print(self.ip + ' 可达！！')
        else:
            print(self.ip + ' 不可达！！')

    def ping(self):
        for i in range(5):
            self.ping_ip = IP(src=self.srcip, dst=self.ip) / ICMP() / (b'x' * self.length)
            self.ping_result5 = sr1(self.ping_ip, timeout=2, verbose=False)
            if self.ping_result5:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)
        print('')

    def __str__(self):
        if self.srcip == None:
            return f'<{self.__class__.__name__} => dstip: {self.ip}, size: {self.length}>'
        else:
            return f'<{self.__class__.__name__} => srcip: {self.srcip}, dstip: {self.ip}, size: {self.length}>'

class NewPing(QYTPING):
    def ping(self):
        self.ping_ip = IP(src=self.srcip, dst=self.ip) / ICMP() / (b'x' * self.length)
        for i in range(5):
            self.ping_result5 = sr1(self.ping_ip, timeout=2, verbose=False)
            if self.ping_result5:
                print('+', end='', flush=True)
            else:
                print('?', end='', flush=True)
        print('')

    def __str__(self):
        if self.srcip == None:
            return f'<{self.__class__.__name__} => dstip: {self.ip}, size: {self.length}>'
        else:
            return f'<{self.__class__.__name__} => srcip: {self.srcip}, dstip: {self.ip}, size: {self.length}>'

if __name__ == '__main__':
    ping = QYTPING('192.168.31.1')
    total_len = 70

    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word))/2), word, s * int((70 - len(word))/2)))
    print_new('print class')
    print(ping)
    print_new('ping one for sure reachable')
    ping.one()
    print_new('ping five')
    ping.ping()
    print_new('set payload length')
    ping.length = 200
    print(ping)
    ping.ping()
    print_new('set ping src ip address')
    ping.srcip = '192.168.31.100'
    print(ping)
    ping.ping()
    print_new('new class NewPing', '=')
    newping = NewPing('192.168.31.1')
    newping.length = 300
    print(newping)
    newping.ping()


