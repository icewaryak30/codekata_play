#ice
s,t,u=map(str,input().split())
v=input()
c=0
l=[s,t,u]
for i in l:
    if i==v:
        c=c+1
print(c)
