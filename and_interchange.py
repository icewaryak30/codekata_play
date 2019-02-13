s=input()
l=list(s.split(' '))
if len(l)>2:
    for i in range(len(l)):
        if l[i]=="and":
            l[i-1],l[i+1]=l[i+1],l[i-1]
print(*l)
