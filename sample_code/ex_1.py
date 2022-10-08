
    print("select upto 10 Tickets:")
   select_tickets=int(input("enter tickets"))
    if select_tickets <= 10 :
        print("tickets Booked. Thankyou")
    else:
        print("you can't give more than 10 or Negative number")
    print("THANKYOU")

def party_night():
    print("You are the Luckey customer Today")
    print("THANKYOU")


def employee(movie,party):
    print("the USer primary_key is: ")
    print("1) Movie \n 2) party")
    choice=int(input("Select Number:"))
    if choice==1:
        print(" the user is eligble for Movie, enjoy the day")
        r1= movie_rulz()
        return r1
    if choice==2:
        print("the user is eligible for Party, enjoy the day")
        return party_night()
    else:
        print("give proper number")
def details(name,qualification):
    n=list(name)
    m=list(qualification)
    pk=""
    if len(n)!=0 and len(m)!=0:
        for each_key in name,qualification:
            pk+=each_key

    print(pk)
    x="myworld"

    if pk.upper()==x.upper():
        return employee(name,qualification)
                # pass
    else:
        print("Thanks for Choosing")
    # return bachelors(name,qualification,pk)



def user_admin(surname,Graduation):

    if len(surname)!=0 and len(Graduation)!=0:
        return details(surname,Graduation)
    # elif len(surname) == 0:
    #     return details_employee(surname,Graduation)
    else:
        print("No details fetched")
surname=str(input('enter name:'))
Graduation=str(input("enter your Graduation: "))
user_admin(surname,Graduation)