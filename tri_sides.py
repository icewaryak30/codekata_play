l=[int(i) for i in input().split()]
x=max(l)
a=0
for i in l:
    if i!=x:
        a+=i
if a>x:
    print("yes")
else:
    print("no")
