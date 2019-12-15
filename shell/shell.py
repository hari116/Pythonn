import os
import sys
import subprocess

# print(argv)
# myCmd = 'ls -la'
# pout = os.popen(myCmd).read()
# print(pout)
#os.system(myCmd)

subprocess.call(['df', '-H'])