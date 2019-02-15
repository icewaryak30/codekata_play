n,m=map(int,input().split())
x=n^m
b=bin(x)
c=0
for i in b:
    if i=='1':
        print(b.count(i))
        c=1
        break
if c==0:
	print('0')
