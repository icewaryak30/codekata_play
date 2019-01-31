n,k=map(int,input().split())
l=[int(i) for i in input().split()]
s=[]
for i in l:
	if i<k:
		s.append(i)
x=sorted(s)
print(*x)
