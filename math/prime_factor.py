#Highest prime factor of n
import sys


# print(sys.argv[1:])
if len(sys.argv[1:]) == 0:
	n=input('Enter num:')
else:
	n=int(sys.argv[1])
#is n a pn??
for i in range(2,n/2):
	if n%i == 0:
		break
else:
	print(n,'is the HPF')	
#else
#factor
for i in range(n/2,2,-1):
	if n%i == 0:
		for j in (2,i):
			if i%j == 0:
				break
		else:
			print(i, 'is the max prime')
			





