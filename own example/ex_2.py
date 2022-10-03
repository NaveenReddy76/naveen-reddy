movie="rrr"
print("wlecome to rrr movie")
price=int(input("enter your amount:"))
if (not price>100) and price<100:
    print("plase take your first class ticket")
elif (not price<100) and price==150:
    print("please take your second class ticket")
elif (not price<150) and price>200:
    print("please take your third class ticket")
else:
    print("please enter correct amount")

