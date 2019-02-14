s=input()
x=[]
s1=""
for i in s:
	if s.count(i)==1:
		x.append(i)
	else:
		x.append(i.upper())
for i in x:
	s1=s1+i
print(s1)
