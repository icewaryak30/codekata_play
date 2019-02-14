n,m=map(int,input().split())
l=[]
x=['a','e','i','o','u']
c=0
for _ in range(n):
    l.append(input().split())
for i in range(len(l)):
    for j in l[i]:
        for k in j:
            if k.casefold() in x:
                c+=1
                break
                break
if c>=m:
    print("yes")
else:
    print("no")
