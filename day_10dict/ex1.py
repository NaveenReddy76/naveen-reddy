dict_val={"first_number:45","sceondnumber:54","thirdnumber:356",}
dict_val_copy=dict_val.copy()
print(dict_val)
print(type(dict_val))
#item assainment
#dict_val["ns"]="myworld"
#print(dict_val)

dict_val.pop("thirdnumber")
print(dict_val)


