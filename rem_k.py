n,k=map(int,input().split())
l=[int(i) for i in input().split()]
for i in range(k):
	l.remove(l[-1])
print(*l)
