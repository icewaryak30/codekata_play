n,k=map(int,input().split())
l=[int(i) for i in input().split()]
c=0
for i in range(len(l)):
	for j in range(len(l)):
		if l[i]+l[j]==k and i!=j:
			c=c+1
			break
	break
if c==1:
	print("yes")
				
else:
	print("no")
