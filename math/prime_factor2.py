#Highest prime factor of n
import sys

# print(sys.argv[1:])
if len(sys.argv[1:]) == 0:
	n=input('Enter num:')
else:
	n=int(sys.argv[1])
# print(n)

factors=[]
for i in range (n,0,-1):
	if n%i == 0:
		factors.append(i)
print(factors)
#finding highest prime factor
for i in factors:
	for j in range(2,i/2):
		if i%j == 0:
			break
	else:
		print(i)
		break	