n,k=map(int,input().split())
for i in range(0,n):
    if k**i==n:
        s="yes"
        break
    else:
        s="no"
print(s)
