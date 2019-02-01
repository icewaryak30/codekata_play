n,k=map(int,input().split())
l=[int(i) for i in input().split()]
c=0
for i in l:
	if l.count(i)==k:
		if c==0:
			print(i,end="")
			c=c+1
		else:
			print("",i,end="")
