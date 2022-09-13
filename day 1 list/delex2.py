k=["kj",87,9.0,66,87,9,7.0,"true""rrkk",9.0,8.7,6,88,9.0,5.0,6.0,45,67,9.0,]
print(k)
print(len(k))
del k[4]
print(k)
k.pop()
print(k)
print(len(k))
k.pop(5)
print(k)
k.append("san")
print(k)
k.extend(["gavi","naveen"])
print(k)
k.insert(8,200)
print(k)
del k[10]
print(k)
print(len(k)) ##


#ex3..
r=['kj', 87, 9.0, 66, 9, "truer" "kk", 9.0, 8.7, 6, 88, 9.0, 5.0, 6.]
print(r)
print(len(r))
del r[8]
print(r)
r.append("dddd")
print(r)
print(len(r)) ##

#ex4..
c=["sangavi","chinnari","raji","naveen","true"]
print(c)
print(len(c))
c.pop(4)
print(c)
print(len(c)) ##

#ex5
l=[6,8.9,8,99,655,14.9999,898,90,6.7]
print(l)
print(l)
l.extend("hh")
print(l)
print(l.index(90))
print(l)