a,b=map(int,input().split())
p=a|b
x=bin(p)
c=0
for i in range(len(x)):
	if x[i]=='1':
		c+=1
print(c)
