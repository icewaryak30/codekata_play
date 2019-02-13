def decimalToBinary(n):
	l=[]
	if(n > 1):
		decimalToBinary(n//2)
	l.append(n%2)
	return l
