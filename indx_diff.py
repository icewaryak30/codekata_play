#ice
n=int(input())
l=[int(i) for i in input().split()]
x=max(l)
y=min(l)
for i in range(len(l)):
	if l[i]==x:
		i1=i
		break
for i in range(len(l)):
	if l[i]==y:
		i2=i
		break
print(i1-i2)
