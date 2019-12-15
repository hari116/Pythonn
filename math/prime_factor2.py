n=input('Enter num:')
factors=[]
for i in range (n,0,-1):
	if n%i == 0:
		factors.append(i)
print(factors)
for i in factors:
	for j in range(2,i/2)