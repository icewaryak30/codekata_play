n=int(input())
x=[int(i) for i in input().split()]
y=[]
for i in range(len(x)-1):
	if x[i+1]%x[i]==0:
		y.append(x[i+1])
print(*y)
