s=input()
l=[]
for i in s:
    if int(i)%2==1:
        l.append(int(i))
if sum(l)%2==1:
    print("O")
else:
    print("E")
