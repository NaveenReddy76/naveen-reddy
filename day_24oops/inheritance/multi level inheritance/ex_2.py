class room:
    def oyo(self):
        self.room='xyz'
        self.room_2='abc'
        print(self.room,self.room_2)

r=room()
r.oyo()


class count(room):
    def rooms_available(self):
        self.place='available'
        self.area='kadapa'
        print(self.place,self.area)

C=count()
C.rooms_available()
C.oyo()

class booking(count):
    def welecome(self):
        self.come='thankyou'
        self.visit-='again'

B=booking()
B.welecome()