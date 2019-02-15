s=input()
x=""
for i in s:
	if i not in x:
		x+=i+str(s.count(i))
print(x)
