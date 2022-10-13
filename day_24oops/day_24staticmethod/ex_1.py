class statics_method:
    x=89
    @staticmethod
    def results():
        first_results=800
        second_results=821
        print(first_results)
        print(second_results)
        print(x)
        print(statics_method.x)
        staticmethod.results()
        staticmethod().results()


class addattion:
    def results(first,second):
        res=first+second
        addattion.results=staticmethod(addattion.results)
        s=addattion.results(9,8)
        print(s)