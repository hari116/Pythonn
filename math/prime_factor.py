#Highest prime factor of n

n=input('Enter num:')
if n==2:
	HPF=2
if n==0:
	HPF='Not Valid'
if n==1:
	HPF=1
else:
	for i in range(n,2,-1):
		print(i)
