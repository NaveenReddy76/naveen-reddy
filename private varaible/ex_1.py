class A:
    def a_objct(self):
        self.__m=45
        self.__s=80
        self.__k=76
        print(self.__m,self.__s,self.__k)


class B(A):
    def b_object(self):
        self.__s=45
        self.__n=60
        self.__r=90
        print(self.__r/self.__n%self.__s)


obj=B()
obj.b_object()
obj.a_objct()