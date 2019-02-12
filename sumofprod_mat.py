n=int(input())
l=[]
x,y=[],[]
p1,p2=1,1
for i in range(n):
    l.append(input().split())
x=[int(l[i][i]) for i in range(len(l))]
y=[int(l[i][j]) for i in range(len(l)) for j in range(len(l)) if (i+j)==len(l)-1]
for i in x:
    p1=p1*i
for i in y:
    p2*=i
print(p1+p2)      
