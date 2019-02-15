s=input()
x=""
for i in s:
	if i!=" ":
		x=x+i
l=len(x)
for i in range(2,l):
	if l%i==0:
		print("no")
		break
else:
	print("yes")
