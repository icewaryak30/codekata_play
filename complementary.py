s=input()
t=input()
x=s+t
for i in x:
    if x.count(i)!=1 or len(x)<26:
        print("non-complementary")
        break
    else:
        print("complementary")
        break
