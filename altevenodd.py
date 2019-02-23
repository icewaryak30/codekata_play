s=input()
c=[]
x=0
for i in range(len(s)-1):
    if int(s[i])%2==0 and int(s[i+1])%2==1:
        c.append(i)
        c.append(i+1)
    elif int(s[i])%2==1 and int(s[i+1])%2==0:
        c.append(i)
        c.append(i+1)
for i in c:
    if c.count(i)!=1:
        x+=1
        c.remove(i)
    else:
        x+=1
print(x)
