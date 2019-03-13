a,b=map(int,input().split())
p=a*b
x=bin(p)
c=0
y=x[2:]
for i in range(len(y)):
	if y[i]=='1' and c==1:
		print(i+1)
		break
	elif y[i]=='1':
		c+=1
