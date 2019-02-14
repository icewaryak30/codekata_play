s=input()
x=[]
for i in s:
	if s.count(i)==1:
		x.append(i)
	else:
		x.append(i.upper())
for i in x:
	print(i,end="")
