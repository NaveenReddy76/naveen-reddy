import getpass
import string
import os


user=["user1","user2","user3"]
pins=['123','2222','3333']
amounts=[1000,2000,3000]
count=0

print("*************************************")
print("*************************************")
print("*************************************")
print("*************************************")
print("*************************************")
while True:
     user=input('\nENTER USER NAME:')
     user=user.lower()
     if user in users:
       if user== users[0]:
           n=0
     elif user == users [1]:
         n=1
     else:
         n=2
     # break
else:
    print('______________________')
    print('**********************')
    print('INVALID USER NAME')
    print('**********************')
    print('______________________')


    while count < 3:
        print('_________________________')
        print('************************')
        pin=input('PLEASE ENTER PIN:')
        print('***********************')
        print('_________________________')
        if pin.isdigit():
            if user == 'user1':
                if pin == pins[0]:
                    break
                else:
                    count +=1
                    print('____________________')
                    print('**********************')
                    print('INVALID PIN')
                    print('**********************')
                    print('________________________')
                    print()



