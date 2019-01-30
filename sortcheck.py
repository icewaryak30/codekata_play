n=int(input())
l=[int(i) for i in input().split()]
x=sorted(l)
if x==l:
    print("yes")
else:
    print("no")
