kilometers=600
print("welecome to RED BUS")
Name=input("please enter your name:")
seat=input("please enter  your seat number:")
while True:
    seat=int(input("please enter your seat:"))
    if(seat<=4 and seat>=30):
        print("your seat number is",seat)
        break
    else:
        print("invalid seat number")
        break

