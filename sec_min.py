n=int(input())
l=[int(i) for i in input().split()]
x=min(l)
l.remove(x)
print(min(l))
