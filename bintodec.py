def bintodec(n):
	r,d,i=0,0,0
	n1=n
	while n!=0:
		r=n%10
		d=d+r*pow(2,i)
		n=n//10
		i=i+1
	return d
num=int(input())
if bintodec(num)%64==0:
	print("yes")
else:
	print("no")
