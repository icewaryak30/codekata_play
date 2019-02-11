l=["a","e","i","o","u"]
s=input()
x,y=[],[]
for i in s:
	if i.casefold() in l:
		x.append(i)
	else:
		y.append(i)
t=""
for i in x:
	t=t+i
for i in y:
	t=t+i
print(t)
