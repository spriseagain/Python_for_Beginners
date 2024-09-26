#Dictionary in Python

"""
Dictinoaries are used to store data values in
key:value pairs

They are unordered mutable(changeable) and don't allow duplicate keys
"""


info = {
    "key":"value",
    "name":"Sooraj",
    "teaching":"python basics",
    "age":25,
    "is_adult":True,
    "code_langugage":["Python","Java","C#"]

}

print(info)
print(type(info))


#Dictionary is mutable but key can not be list or dictionary. It can be a tuple as it's immutable

#Dictionary is unordered

# We can't repeat keys

print(info["code_langugage"])

info["name"] = "Siraj" #reassigning the new value to key name
info["surname"] = "Pandey" #adding a new key value pair
info["age"]="Twenty Five"  # any type of new data can be assigned

print(info)


#creating an empty dictionary
null_dict ={}


# Nested Dictionary

student = {
    "name":"Sooraj Pandey",
    "subjects":{"phy":97,
                "chem":98,
                "bio":87}
}

print(student)


#Methods in dictionary

# 1. dict.keys()
print(list(student.keys())) 

print(len(list(student.keys())))

print(len(student))

# 2. dict.values()
print(list(student.values())) 

print(len(list(student.keys())))

#3.dict.items() -- returns all key:val piairs as tuples

print(list(student.items()))

#4 dict.get("key") method

# print(student["name2"])  #error --> this throws error

print(student.get("name2"))


student.update({"city":"delhi"}) #--> gives none value -- doesn't create a new dictionary


student_new = {"name":"spriseagain","grade":"A","city":"london"}
student.update(student_new)

print(student)




