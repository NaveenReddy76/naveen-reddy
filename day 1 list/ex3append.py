a=["s", 2.2, 9.0, 6, "false", 3.2, 4.7, 9.0, "true", "naveen"]
print(type)
print(len(a))
a.append("naveen")
print(a)
a.append("true")
print(a)
print(len(a)) #


b=["s", 2.2, 9.0, 6, "false", 3.2, 4.7, 9.0, "true", "naveen"]
print(type)
print(len(b))
b.pop(5)
print(b)
print(len(b))
print(b.index(4.7))
print(b)


c=["s", 2.2, 9.0, 6, "false", 3.2, 4.7, 9.0, "true", "naveen"]
print(c)
print(len(c))
c.extend("s",)
print(c)
print(c.index(6))
print(c)
print(len(c))
c.extend(["c","f",9]) #



d=["s", 2.2, 9.0, 6, "false", 3.2, 4.7, 9.0, "true", "naveen"]
print(type)
print(len(d))
print(d[0])
print(d[8])
d.insert(5,45)
print(len(d))


e=[]
f=["s", 2.2, 9.0, 6, "false", 3.2, 4.7, 9.0, "true", "naveen"]
print(e)
print(f)
print(f[3])
e.append(f)
print(e)
e.append(f[0::])