jk={"name","keyboard","python","sql","java","c++","langague"}
print(type(jk))
print(jk)
print(len(jk))
jk.discard("name")
print(jk)
print(len(jk))


#ex2
jk={4.7,8.9,76.9,8.0,9.0,7.0,4.8,3.67,7.7,8.1,9.2,6.4}
print(type(jk))
print(jk)
print(len(jk))
jk.discard(8.9)
jk.discard(8.0)
print(jk)
print(len(jk))
jk.discard(8.9)
print(jk)

#ex3
jk={45,65,76,965,767,98,69,89,98,787,98988,565,3453,9898,345,56}
print(type(jk))
print(jk)
print(len(jk))
jk.discard(98)
jk.discard(787)
print(jk)
print(len(jk))
jk.discard(98)
print(jk)

#ex4
jk={43,5,24,"kefn","fe","false",9.0,34,4.5,24,5.1,9.0,49,"lhwqkj"}
print(jk)
print(len(jk))
jk.discard("false")
jk.discard("fe")
jk.discard(9.0)
print(jk)
print(len(jk))
jk.discard("fe")
print(jk)
