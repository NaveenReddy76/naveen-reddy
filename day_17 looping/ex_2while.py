#laptop=hp
x=60000
while x<85000:
    print(x)
    break
balance=int(input("enter your balance:"))
if balance<60000 or balance>85000:
    print("sufficent balance")
print("welecome to hp laptop store")
price=int(input("enter a value:"))
if price<=45000 or price<=100000:
    print("available")
else:
    print(" sorry laptop is not available")