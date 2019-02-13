n=int(input())
c=0
for i in range(n+1):
	if (i*3)==n:
	    c+=1
	elif (i*7)==n:
		c+=1
	elif (i*3)+(i*7)==n:
		c+=1
if c!=0:
	print("yes")
else:
	print("no")
