# !/usr/bin/python3.8
# -*- coding=utf-8 -*-

from Python_9_1 import *

import re

def ssh_get_route(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command('route -n')
    route_n_result = stdout.read().decode()
    route_gateway = re.match(r'[\S\s]+0\.0\.0\.0\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})[\S\s]+UG[\S\s]+', route_n_result).groups()
    return route_gateway[0]


if __name__ == '__main__':
    print(qytang_ssh('192.168.31.62', 'root', '!ningzhe305'))
    print(qytang_ssh('192.168.31.62', 'root', '!ningzhe305', cmd='pwd'))
    print('网关为：')
    print(ssh_get_route('192.168.31.62', 'root', '!ningzhe305'))
