mobile="oneplus"
print("welecome to oneplus monile store")
store_price=int(input("please enter your mobile price:"))
balance=int(input("enter ur balance:"))
if store_price<25000 or store_price>55000:
    print(" please enter correct price")
    if balance<65000 or balance>85000:
       print("the amount was not sufficent")
    else:
       print("enter your amount")
elif balance==65000 or balance==85000:
    print("the amount once you need to check")
elif store_price==25000 or store_price==55000:
    print("please check once again")
elif balance<=65000 or balance>=85000:
    print("the amount was suffiecnt")
else:
    print("the amount was available ")