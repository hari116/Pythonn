import sys
import cred
import json

#print(sys.argv[1:])
# f=open('cred.txt', 'r')
# if f.mode =='r':
# 	contents=f.read()
# print(contents)	
#print(cred.x)

f=open('cred.json')
obj = json.load(f)
print(obj['b'])
f.close()