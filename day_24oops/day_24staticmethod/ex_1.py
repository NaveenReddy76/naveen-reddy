class statics_method_ss:
    x=89
    @staticmethod
    def results():
        first_results=800
        second_results=821
        print(first_results)
        print(second_results)
        print(first_results+second_results)
       # print(x)    # error
        print(statics_method_ss.x)
statics_method_ss.results()

class addattion:
    def results(first,second):
        res=first+second
        addattion.results=staticmethod(addattion.results)
        print(res)
        #s=addattion.results(9,8)
       # print(s)

addattion.results(22,22)




#
def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            return max_num