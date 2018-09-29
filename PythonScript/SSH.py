import paramiko
import os
paramiko.util.log_to_file('syslogin.log')

host='192.168.0.127'
user='root'
passwd='mysqlpassword'
port=22

def connet_by_key(host,user,port=22):
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        pkey='C:\\Users\\mayn\\.ssh\\id_rsa.pub'
        client.connect(hostname=host,username=user,port=port,key_filename=pkey)
        stdin, stdout, stderr = client.exec_command('free -m')        #执行命令
        print(stdout.read().decode('utf-8'))

def connet_by_passwd(host,user,passwd,port=22):
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host,username=user,port=port,password=passwd)
        stdin, stdout, stderr = client.exec_command('ip addr')           #执行命令
        print(stdout.read().decode('utf-8'))

def transport_by_sftp(host,user,passwd,port=22):
    t=paramiko.Transport((host,port))
    t.connect(username=user,password=passwd)
    sftp = paramiko.SFTPClient.from_transport(t)
    try:
        sftp.put()
        sftp.get()
    except:
        print('error')

if __name__ == '__main__':
    connet_by_passwd(host=host,user=user,passwd=passwd)