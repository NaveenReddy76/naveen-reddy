def cls():
    global x
    x=10000
    print("global v:",x)
cls()
print(x)


#
def cls_1(n,s,c,l,r):
    global x
    x=10
    print("global v:",x)
    print(n)
    print(c)
    print(r)
    print(s)
    print(l)
cls_1(2334,5445,6755,9809,9809)


#
match=45
hitman=100
virat=100
def score():
    global m
    m=100
    print("global match:",m)
    print(hitman)
score()
print(virat)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&/n&&&&&&&&&&&&&&&&&")
print(match)