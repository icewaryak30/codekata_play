vow=["a","e","i","o","u"]
s=input()
c=0
x=[]
if len(s)<2:
	print(0)
else:
	for i in range(0,len(s)-1,2):
		if s[i] in vow and s[i+1] not in vow or s[i] not in vow and s[i+1] in vow:
			c+=2
			x.append(c)
		else:
			c=0
			x.append(c)
	print(max(x))
