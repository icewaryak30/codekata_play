s1,s2=map(str,input().split())
x=len(s1)
y=len(s2)
n=max(x,y)
c=0
for i in range(1,n):
    if x%i==0 and y%i==0:
        c=c+1
if c==1:
    print("yes")
else:
    print("no")
