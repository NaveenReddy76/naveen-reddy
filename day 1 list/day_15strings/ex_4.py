# swap first and last character
string="this is python string class"
x=list(string)
temp=x[0]
x[0]=x[-1]
x[-1]=temp
print("".join(x))


#
def change_sring(str1):
    return str1[:]
print(change_sring("this is python string class"))
