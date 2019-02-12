l=["R","P","S"]
s=input().split()
if "R" in s and "P" in s:
    print("P")
elif "P" in s and "S" in s:
    print("S")
elif "R" in s and "S" in s:
    print("R")
else:
    print("D")
