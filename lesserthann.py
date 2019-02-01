n=int(input())
l=[int(i) for i in input().split()]
s=[]
for x in l:
	if x<n:
		s.append(x)
print(*s)
