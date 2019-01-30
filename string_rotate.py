n,k=map(str,input().split())
s=[i for i in n]
l=[]
for a in range(int(k)):
    x=s[-1]
    l.append(x)
    s.remove(x)
for i in range(len(l)-1,-1,-1):
    print(l[i],end="")
for i in s:
    print(i,end="")
