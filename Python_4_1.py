if __name__ == '__main__':
    pass


import os
import re
ifconfig_result = os.popen('ifconfig ' + 'ens33').read()

# 正则表达式查找ip，掩码，广播和mac地址
ipv4_add = re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', ifconfig_result)[0]
netmask = re.findall(r'255\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', ifconfig_result)[0]
broadcast = re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.255', ifconfig_result)[0]
mac_addr = re.findall(r'[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}\:[0-9a-f]{2}', ifconfig_result)[0]

# 格式化字符串
format_string = '{0:<10}:{1:<20}'

# 打印结果
print(format_string.format('ipv4_add', ipv4_add))
print(format_string.format('netmask', netmask))
print(format_string.format('broadcast', broadcast))
print(format_string.format('mac_addr', mac_addr))

# 产生网关的IP地址
ipv4_gw = re.sub('.62', '.1', ipv4_add)

# 打印网关的IP地址
print('\n我们假设网关IP地址为最后一位为1，因此网关IP地址为：' + ipv4_gw + '\n')

# Ping网关
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()

re_ping_result = re.match(r'[\s\S]*\s0\%', ping_result)

if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')


