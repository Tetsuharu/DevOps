
import paramiko
import time

def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)
        chan = ssh.invoke_shell()
        x = chan.recv(2048).decode()
        print(x)
        chan.send('enable\n'.encode())
        chan.send(enable.encode())
        for y in cmd_list:
            chan.send(y.encode())
            time.sleep(wait_time)
            z = chan.recv(2048).decode()
            if verbose:
                print(z)
            else:
                pass

    except Exception:
        pass

if __name__ == '__main__':
    cmd_list = ['ter len 0\n', 'show ver\n', 'conf t\n', 'router ospf 1\n', 'network 192.168.31.0 0.0.0.255 area 0\n', 'end\n']
    # enable没有密码的情况
    qytang_multicmd('192.168.31.200', 'admin', 'Cisc0123', cmd_list)
    # enable有密码的情况
    # qytang_multicmd('192.168.31.200', 'root', 'cisco', cmd_list, enable='cisco\n')


