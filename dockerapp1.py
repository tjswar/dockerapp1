def numrotate(a,n):
	for i in range(n):
		for j in range(len(a)):
			a[j],a[len(a)-1]=a[len(a)-1],a[j]
	return a
n=numrotate([1,2,3,4,5],2)
print(n)