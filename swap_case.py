s=input()
g=[]
for i in s:
    if i.isupper():
        g.append(i.lower())
    else:
        g.append(i.upper())
for i in g:
    print(i,end="")
