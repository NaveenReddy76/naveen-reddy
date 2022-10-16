class bike:
    def bike_details(self):
        self.model='ZMR'
        self.year='2016'
        self.price='166000'
        self.cc='250'
        print(self.model)
        print(self.year)
        print(self.price)
        print(self.cc)
    def bike_showrooms(self):
        self.firstshowroom='kadapa'
        self.secondshowroom='rayachoty'
        print(self.firstshowroom,self.secondshowroom)

b=bike()
b.bike_details()
b.bike_showrooms()


print("__________________________________________")


class motor(bike):
    def motor_models(self):
        self.motornumber='4568778'
        self.warranty='5 years'
        print(self.warranty)
        print(self.motornumber)
    def motor_company(self):
        self.company_1="naveen"
        self.company_2="haveels"
        print(self.company_1)
        print(self.company_2)

M=motor()
M.motor_models()
M.motor_company()
M.bike_details()
M.bike_showrooms()


