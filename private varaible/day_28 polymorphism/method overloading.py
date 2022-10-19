class A:
    def volume(self,number_1,number_2,number_3):
        self.first='number_1'
        self.second='number_2'
        self.third='number_3'
        print(self.first,self.second,self.third)

class B(A):
    def volume(self,sangavi,naveen,dosxy):
        self.option_1="sangavi"
        self.option_2='naveen'
        self.option_3='dosxy'
        print(self.option_1,self.option_2,self.option_3)


class c(B):
    def number(self,number_1,number_2,number_3):
        self.nu=number_1
        self.nu2=number_2
        self.nu3=number_3
        print(self.nu,self.nu2,self.nu3)

class d(c):
    def laptop(self):
        self.lapstore="hp"
        self.location='kadapa'
        self.cost='55,000'
        print(self.lapstore,self.cost,self.location)


obj=d()
obj.laptop()
obj.number(45,55,67)
obj.volume("hello","hru","good dog")
obj.volume("hi","hihiiiii","jkkkkkk")