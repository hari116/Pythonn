from smtplib import SMTP_SSL
from sys import argv
import base64

message = base64.b64decode(argv[1])
from_email = "sibro-backup@protracked.in"
to_email = ["hari.protracked@gmail.com" , 'alerts@protracked.in']
email_text = """\
From: %s
To: %s
Subject: Disk Usage
%s
""" % (from_email, ','.join(to_email), message.decode('ascii'))

with SMTP_SSL('email-smtp.eu-west-1.amazonaws.com', 465) as smtp:
    smtp.ehlo()
    smtp.login("AKIA4OENZTZF3462AWLZ", "BBV2qD5jnKNTp5vIDuX+Mf+dUSSHv7/fR56UnPbyyIG+")
    smtp.sendmail(from_email, to_email, email_text)