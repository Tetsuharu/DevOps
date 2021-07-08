# !/usr/bin/python3.8
# -*- coding=utf-8 -*-

import paramiko

def qytang_ssh(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

if __name__ == '__main__':
    print(qytang_ssh('192.168.31.62', 'root', '!ningzhe305'))
    print(qytang_ssh('192.168.31.62', 'root', '!ningzhe305', cmd='pwd'))
