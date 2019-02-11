l=["a","e","i","o","u"]
n=int(input())
x,y=[],[]
d={}
for i in range(n):
	x.append(input())
for i in x:
	c=0
	for j in i:
		if j.casefold() in l:
			c=c+1
	y.append(c)
	d.update({i:c})
m=sorted(y,reverse=True)
for i in m:
    for k,v in d.items():
	    if v==i:
	        print(k)
