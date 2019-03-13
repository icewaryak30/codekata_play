s=int(input())
x=[]
for i in range(s):
	x.append(input())
for k in range(len(x)-1):
	if x[k]==x[k+1]:
		p="yes"
		break
	else:
		p="no"
print(p)
