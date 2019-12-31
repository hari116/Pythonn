#!/bin/sh
from smtplib import SMTP_SSL
from sys import argv
import subprocess

A=["hostname; date; echo 'df -h'; df -HT --type=ext4;"]
#print(argv[1:])
message = subprocess.check_output(A,shell=True)
#print(message.decode('ascii'))
# message = "".join(argv[1:])
from_email = "sibro-alerts@protracked.in"
to_email = ["hari.protracked@gmail.com" , 'alerts@protracked.in', 'vivekstanley@protracked.in' , 'shinepro@protracked.ml']
subject = 'Disk Usage'
email_text = """\
From: %s
To: %s
Subject: %s

<span>
%s
</span>
""" % (from_email, ','.join(to_email), subject, message.decode('ascii'))

with SMTP_SSL('email-smtp.eu-west-1.amazonaws.com', 465) as smtp:
    smtp.ehlo()
    smtp.login("AKIA4OENZTZF3462AWLZ", "BBV2qD5jnKNTp5vIDuX+Mf+dUSSHv7/fR56UnPbyyIG+")
    smtp.sendmail(from_email, to_email, email_text)

