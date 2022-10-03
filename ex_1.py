balance=50000
print("\t \t \t welecome to INDIAN BANK ATM")
Name=input("please enter your name :")
while True:
 pin=int(input("please enter your pin:"))
 if(pin<1000 or pin>9999):
     print("please enter a valid pin number")
     break
 else:
     pass
 account=int(input("please select y our account type \n1:saving\n2:current"))
 if(account==1):
     choose=int(input("selct your option \n1:withdraw\n2:balance enquiry\n3:deposit"))
     if(choose==1):
         amount=int(input("please enter the amount"))
         if(amount<0 or amount>balance):
             print("please enter valid amount")
         elif(amount<=balance):
             print("your request is procesing")
             print("please take your amount")
             print("THANK YOU")
             print("VISIT AGAIN")
             break
         elif account==2:
             print("you have not current account")
             break
         else:
             print('choose correct option break')
