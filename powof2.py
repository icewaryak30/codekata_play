n=int(input())
for i in range(0,n):
    if 2**i==n:
        s="yes"
        break
    else:
        s="no"
print(s)
