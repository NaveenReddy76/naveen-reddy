ss={2.9,0,99,"true","ab",3,4,66,97,9.0,8.7,21,1}
print(type(ss))           #<class 'set'>
print(ss)            #{0, 97, 'ab', 2.9, 99, 3, 4, 'true', 66, 9.0, 8.7, 1, 21}
print(len((ss)))     #13

#exadd
ss={2.9,0,99,"true","ab",3,4,66,97,9.0,8.7,21,1}
print(ss)         #{0, 97, 'ab', 2.9, 99, 3, 4, 'true', 66, 9.0, 8.7, 1, 21}
ss.add("false")
print(ss)         #{0, 97, 'ab', 2.9, 99, 3, 4, 'true', 66, 9.0, 8.7, 1, 'false', 21}
ss.add("kkk")
ss.add("mmm")
print(ss)        #{0, 97, 'ab', 2.9, 99, 3, 4, 'true', 66, 9.0, 8.7, 1, 'mmm', 'false', 21, 'kkk'}
print(len(ss))  #16

#exremove
ss={2.9,0,99,"true","ab",3,4,66,97,9.0,8.7,21,1}
print(ss)      #{0, 97, 'ab', 2.9, 99, 3, 4, 'true', 66, 9.0, 8.7, 1, 21}
ss.remove(97)
print(ss)       #{0, 'ab', 2.9, 99, 3, 4, 'true', 66, 9.0, 8.7, 1, 21}
ss.remove("true")
print(ss)            #{0, 'ab', 2.9, 99, 3, 4, 66, 9.0, 8.7, 1, 21}
print(len(ss))      #11

#exupdate
ss={2.9,0,99,"true","ab",3,4,66,97,9.0,8.7,21,1}
print(ss)                #{0, 97, 'ab', 2.9, 99, 3, 4, 'true', 66, 9.0, 8.7, 1, 21}
ss.update(["python","my_world","kkk"])
print(ss)                #{0, 97, 'ab', 2.9, 99, 3, 4, 'true', 66, 9.0, 8.7, 1, 'python', 21, 'my_world', 'kkk'}
print(len(ss))          #16

#exdiscard
ss={2.9,0,99,"true","ab",3,4,66,97,9.0,8.7,21,1}
print(ss)                #{0, 97, 'ab', 2.9, 99, 3, 4, 'true', 66, 9.0, 8.7, 1, 21}
ss.discard("ab")
print(ss)                #{0, 97, 'ab', 2.9, 99, 3, 4, 'true', 66, 9.0, 8.7, 1, 21}
ss.discard("python")     #{0, 'true', 2.9, 99, 3, 4, 66, 97, 8.7, 9.0, 1, 21}
print(ss)               #{0, 'true', 2.9, 99, 3, 4, 66, 97, 8.7, 9.0, 1, 21}


#pop
ss={2.9,0,99,"true","ab",3,4,66,97,9.0,8.7,21,1}
print(ss)                    #{0, 97, 2.9, 99, 3, 4, 66, 1, 8.7, 9.0, 'true', 21, 'ab'}
ss.pop()
print(ss)                    #{97, 2.9, 99, 3, 4, 66, 1, 8.7, 9.0, 'true', 21, 'ab'}

