dict_val={"firstname":"user_1","secondname":"user_2","thirdname":"user_3"}
print(dict_val["firstname"])
print(dict_val['secondname'])
print(dict_val.keys())
print(dict_val.items())
dict_val["firstname"]="naveen"
print(dict_val)
dict_val.pop("secondname")
print(dict_val)



#
nested_dict={"first":{"g":76,"h":56},
            "second": [89,9,78,"hgh"],
             "third":(677,87,98,"j"),
             "set":{1,2,4,4,3,5,6,7,5,6,8,9}}
print(nested_dict["first"])
print(nested_dict.values())
print(nested_dict["first"]["g"])
print(nested_dict.get("first").get (80))

