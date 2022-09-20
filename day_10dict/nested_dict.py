nested_dict={"naveen":{45:"hitman",18:"virat",17:"abd",25:"dhwan",100:"hardik"},
             "san":[94,"hkkb",898.9,"ran","five","ubu",909],
             "third":("a","b",1,2,3,4,5,6,5,6,),
             "fourth":{"sangavi",989,787,989,989,"bb","lklk"},
             "fifth":{"job":"jkj","place":"rayachoty","distcrit":"kadapa"}}

print(nested_dict["naveen"])
print(nested_dict["fifth"])
print(nested_dict["san"])
print(nested_dict["third"])
print(nested_dict["fourth"])
print(nested_dict.get("san"))
print(nested_dict.pop("fifth"))
print(nested_dict.update())
print(nested_dict.popitem())
print(nested_dict.keys())
print(nested_dict.values(),"=====================================")
print(len(nested_dict),"*****************************")
print(nested_dict.__or__("third"))
print(nested_dict.__doc__)
print(nested_dict.__str__())
print(nested_dict.__len__(),"========================")
print(nested_dict.__setitem__("san","naveen"))

