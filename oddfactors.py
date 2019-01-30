#ice
n=int(input())
l=[]
c=0
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for i in range(0,len(l)):
    if l[i]%2==1:
        c=c+1
        if c==1:
            print(l[i],end="")
        else:
            print("",l[i],end="")
