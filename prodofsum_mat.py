n=int(input())
l=[]
x,y=[],[]
s1,s2=0,0
for i in range(n):
    l.append(input().split())
x=[int(l[i][i]) for i in range(len(l))]
y=[int(l[i][j]) for i in range(len(l)) for j in range(len(l)) if (i+j)==len(l)-1]
s1=sum(x)*sum(y)
print(s1)      
