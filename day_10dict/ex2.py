dictt={}

dictt["python"]="45 days"
dictt["django"]=40
dictt["mysql"]=17
print(dictt)

dictt.popitem()
print(dictt)
del dictt["python"]
print(dictt)
dictt_copy=dictt.copy()
print(dictt)
dictt.get("django:40")
print(dictt)
dictt.items()
print(dictt)
dictt.pop("django")
print(dictt)
