s,t=map(str,input().split())
if len(t)>len(s):
    print("no")
elif t in s:
    print("yes")
else:
    print("no")
