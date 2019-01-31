n=int(input())
s=[int(i) for i in input().split()]
t=[int(i) for i in input().split()]
l=[]
for a in s:
	for b in t:
		if a==b:
			l.append(a)
			t.remove(b)
print(*l)
