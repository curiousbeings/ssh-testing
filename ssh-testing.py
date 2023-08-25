import paramiko

hostname='127.0.0.1'
port=22
user='ishav'
passd=''
try:
    client=paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname,port,username=user,password=passd)
    print(client.exec_command('pwd')[1].read().decode())

    client.close()
except Exception as e:
    print(str(e))
