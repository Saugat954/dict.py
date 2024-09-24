#Dictionary in python

info = {
    "Name":"Saugat",
    "Age":22,
    "city":"Brisbane",
    "Education":"Bachelor degree"
}

print(info)
print(info.get("Age"))
print(info["Name"])

#Accessing multiple values in a dictionary

print(info.keys())
print(info.values())

#looping through a dictionary\
for key in info:
    print(key)

for value in info.keys():
    print(info[value])

for char in info["Name"]:
    print(char)


for key , value in info.items():
    print(f"the value of {key} is {value}")


#dictionary method
#update


class1 = {
    122 : 45,
    123 : 89,
    124 : 90,
    125 : 55

}
class2 = {
    126 : 54,
    127 : 49,
    128 : 80,
    129 : 65

}
#adding in dictionary
class1.update(class2)
print(class1)

#popitem method removes the last item
class2.popitem()

#.clear() makes the dictionary empty
class2.clear()
#deleting the dictionary
del class2