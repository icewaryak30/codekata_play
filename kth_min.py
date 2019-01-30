n,k=map(int,input().split())
l=[int(i) for i in input().split()]
for i in range(0,k-1):
    x=min(l)
    l.remove(x)
print(min(l))
