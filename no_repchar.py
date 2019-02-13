s=input()
x=""
if s.isalpha():
	for i in s:
		if i not in x:
			x=x+i
print(x)
