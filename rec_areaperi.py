p,a=map(int,input().split())
c=0
for i in range(1,a):
    for j in range(1,a):
        if 2*(i+j)==p and i*j==a:
            s="yes"
            c+=1
            break
if c==0:
    s="no"
print(s)
