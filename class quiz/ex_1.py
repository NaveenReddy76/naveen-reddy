s=int(input("enter any number :"))
n=[int(a) for a in str (s)]
if len(s) == 5:
    if [n[0]+n[4]%2]==0:
        c=n[1]**3+n[3]**3
        print(c)
    else:
        d=n[1]**2+n[3]**2
        print(d)
else:
    print("the value should be 5 digits number ")