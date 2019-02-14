n,m=map(int,input().split())
x=n^m
b=bin(x)
for i in b:
    if i=='1':
        print(b.count(i))
        break
