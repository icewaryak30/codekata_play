l=["A","B","C","D","E","F"]
s=input()
for i in s:
    if i in l:
        r="yes"
    elif i.isdigit():
        r="yes"
    else:
        r="no"
        break
print(r)
