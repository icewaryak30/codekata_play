n,k=map(int,input().split())
x=[int(i) for i in input().split()]
y,z,a=[],[],[]
for i in range(len(x)):
	if (i+1)<=k:
		y.append(x[i])
	else:
		z.append(x[i])
for i in sorted(y):
	a.append(i)
for i in sorted(z,reverse=True):
	a.append(i)
print(*a)
