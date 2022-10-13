# if without using of  lambda

def largest_value(s,n,c):
    if s>n and s>c:
        print("a is greater:")
    elif n>s and n>c:
        print("n is gretaer:")
    else:
        print("c is greater:")
largest_value(45,25,7)
largest_value(19,43,76)
largest_value(43,899,67)


# if using with lambda

lambda x,y,z: