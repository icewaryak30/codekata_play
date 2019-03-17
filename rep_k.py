n,k=map(int,input().split())
x=[int(i) for i in input().split()]
for i in x:
	if x.count(i)==k:
		print(i)
		break
