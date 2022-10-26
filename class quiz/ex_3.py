
from functools import reduce
count=0
values =[]
x= input("enter values: ")
result_val=x.split(" ")
data = results_val

for each in data:

    values.append(int(each))
count+=len(x)
c = reduce(lambda a,b:a+b, values)

print(count)
print(c)