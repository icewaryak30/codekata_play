a,b,c=map(int,input().split())
l=[a,b,c]
for i in l:
    if i==0:
        print("no")
        break
else:
    if (a+b+c)==180:
        print("yes")
    else:
        print("no")
