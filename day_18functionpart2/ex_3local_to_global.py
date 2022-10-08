x=789
y=9898
z=8889
def num():
    y=9898
    print("local num:",y)
    print("global num:",x)
    print("global num:",z)
num()
print(x)
print( y)
print(z)


#
x=4545
y=6767
z=9898
def values(x,y,z):
    z=8887
    print("global value:",z)
values(4545,6767,9898)
print("__________________________/n________________")
print(x)
print(y)
print(z)


#
x=4545
y=6767
z=9898
def values(x,y,z):
    z=8887
    print("global v:",z)
    print("********************************/n******************")
    print(globals()["z"])
values(4545,6767,9898)
print(x)
print(y)