

class Emp:
    data = " The emp details are: "
    def setdetails(self, name, id):
        self.name = name
        self.id = id

    def getdetails(self):
        print(self.name)
        print(self.id)


E = Emp()
E.setdetails("User_1", "101mw")
E.getdetails()
print(E.data)
print(Emp.data)