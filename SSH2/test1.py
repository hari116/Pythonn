import paramiko

ip='167.71.232.152'
port=22
username='root'
password='@cold#spring112'

cmd1='hostname' 
cmd2='ll'

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)

stdin,stdout,stderr=ssh.exec_command(cmd1)
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)

stdin,stdout,stderr=ssh.exec_command(cmd2)
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)
