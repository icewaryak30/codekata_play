a,b=map(int,input().split())
p=a*b
x=bin(p)
y=x[::-1]
for i in range(len(y)):
	if y[i]=='1':
		print(i+1)
		break
