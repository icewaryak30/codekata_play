n=int(input())
l=[int(i) for i in input().split()]
x=[]
for i in l:
    if l.count(i)==1:
        x.append(i)
print(*x)
