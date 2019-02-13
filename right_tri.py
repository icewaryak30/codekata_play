l=[int(i) for i in input().split()]
x=max(l)
c,d=0,0
for i in l:
    if i==x:
        d=i**2
    else:
        c=c+i**2
if c==d:
    print("yes")
else:
    print("no")
