n=int(input())
l=[int(i) for i in input().split()]
for i in l:
	if i==0:
		l.remove(i)
		l.append(i)
print(*l)
