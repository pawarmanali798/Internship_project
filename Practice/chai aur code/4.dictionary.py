myDict={
    "name":"Manali",
    "school":"jpems",
    "college":"sitcoe"
}
print(myDict)

print(myDict["school"])
# myDict["child"]=input("Enter your child name:")
print(myDict)
print(myDict.get("name"))
print("--------------------")

#accessing key:
for x in myDict:
    print(x)

# acesss items:
for x in myDict:
    print(x,myDict.get(x))

#access items i.e:key,value
for key,value in myDict.items():
    print(key,value)

print("------------------")

#pop value
print(myDict.pop("college"))

#popitems
print(myDict.popitem())  #('school', 'jpems')

myDict["school"]="jpems"
print(myDict)

print("~~~~~~~~~~~~~~~~")

# dict comphrension
newDict={x:x**4 for x in range(10)} #{0: 0, 1: 1, 2: 16, 3: 81, 4: 256, 5: 625, 6: 1296, 7: 2401, 8: 4096, 9: 6561}
print(newDict)

print("++++++++++++")

waterkeys=["ice","water","steam"]
watervalues="cool"
waterDict=dict.fromkeys(waterkeys,watervalues)
print(waterDict)
