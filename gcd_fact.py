a,b=map(int,input().split())
g=min(a,b)
f=1
for i in range(1,g+1):
	f=f*i
print(f)
