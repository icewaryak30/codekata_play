s,n=map(str,input().split())
x=""
for i in range(len(s)):
	if (i+1)%int(n)==0:
		x+=s[i].upper()
	else:
		x+=s[i]
print(x)
