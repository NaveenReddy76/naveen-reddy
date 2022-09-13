a=[2,4,87,9.9,"truie","d",7.0,45,2,]
print(type)
print(len(a))
a.append(2)
print(a)
print(len(a))


b=[2,4,87,9.9,"truie","d",7.0,45,2,]
print(type)
print(len(b))
b.pop()
print(b)
b.pop(3)
print(len(b))
print(b.count(2))

c=[2,4,87,9.9,"true","d",7.0,45,2,]
print(type)
print(len(c))
c.extend(["c",45,25])
print(c)
print(len(c))
print(c.index("true"))
print(c[4])


d=[2,4,87,9.9,"true","d",7.0,45,2]
print(type)
print(len(d))
d.insert(4,45)
print(d)
d.insert(3,"naveen")
