s,t=map(str,input().split())
c=0
for i in s:
    for j in t:
        if i==j:
            c+=1
            break
if c!=0:
    print("yes")
else:
    print("no")
