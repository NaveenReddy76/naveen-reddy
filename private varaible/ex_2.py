class university:
    def university_details(self):
        self.__groups="all degrere groups are avialble"
        self.__strenth=400
        self.location="TIRUPATHI"
        print(self.__groups,self.location,self.__strenth)
        print("<><<><><><><><><><><>><<><><><><>><><>><><><><>")

class collage(university):
    def yogi_vemana_(self):
        self.__loc="Kadapa"
        self.__postion=1
        self.__no_of_teachers=45
        print(self.__loc,self.__postion,self.__no_of_teachers)
        print("???????????????????????????????????????????????????")

class collage_2(collage):
    def CRRRDC(self):
        self.__loc="RAYACHOTY"
        self.__postion=3
        self.__no_of_empolyess=20
        print(self.__loc,self.__postion,self.__no_of_empolyess)
        print("_________________________________________")


class collage_3(collage_2):
    def prathibha_junior_clg(self):
        self.__groups="MPC,BIPC"
        self.__mpsstrenth='200'
        self.__bipsstre='120'
        print(self.__groups,self.__mpsstrenth,self.__bipsstre)
        print("**********************************************")

obj=collage_3()
obj.university_details()
obj.CRRRDC()
obj.prathibha_junior_clg()
obj.yogi_vemana_()