
import paramiko

def qytang_ssh(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


# Line1 = '计算'+str(1)+ ' + '+str(2)+'的结果'
# Line2 = '计算结果为：' + str(1+2)
#
# print(Line1)
# print(Line2)



list_ip = '''
R2#show ip int brief
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                10.1.1.1        YES manual up                    up
Ethernet0/1                192.168.1.1     YES manual administratively down down
Ethernet0/2                172.16.1.1      YES manual administratively down down
Ethernet0/3                unassigned      YES unset  administratively down down
Ethernet1/0                unassigned      YES unset  administratively down down
Ethernet1/1                unassigned      YES unset  administratively down down
Ethernet1/2                unassigned      YES unset  administratively down down
Ethernet1/3                unassigned      YES unset  administratively down down
Loopback0                  2.2.2.2         YES manual up                    up
'''