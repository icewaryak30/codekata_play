def fact(m):
	f=1
	for i in range(1,m+1):
		f=f*i
	return f
x=int(input())
c=0
l=[]
#print(fact(x))
for i in range(x+1):
	cat=fact(2*i)//(fact(i+1)*fact(i))
	l.append(cat)
print(*l)
