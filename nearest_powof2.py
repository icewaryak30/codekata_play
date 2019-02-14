def bin_dec(n):
    num=0
    x=list(str(n))
    y=x[::-1]
    for i in range(len(y)):
        if y[i]=='1':
            num+=pow(2,i)
    return num
def power(b):
    for i in range(b):
        if 2**i==b:
            return 1
    else:
        return 0
n=int(input())
b=bin_dec(n)
print(b)
while power(b)==0:
    b+=1
print(b)
