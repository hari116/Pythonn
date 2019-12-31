import paramiko

host='app.sibro.xyz'
p=22

ssh = paramiko.SSHClient()
ssh.connect(host, port=p, timeout=2)
cmd = "ls"
stdin, stdout, stderr = ssh.exec_command(cmd)
for line in stdout.readlines():
    print(line)
ssh.close()
