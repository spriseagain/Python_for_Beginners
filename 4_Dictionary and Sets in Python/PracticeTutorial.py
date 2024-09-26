# Practice problems

#1. Store following word meaning in dictionaru
'''
table:"a piece of furniture", "list of fact and figures"
cat: "a small animal"

'''

dict = {"table":["a piece of furniture", "list of fact and figures"],"cat":"a small animal"}
print(dict)
print(type(dict))


#2 Given list of sub for students
'''
Assume one classroom is required for 1 subject.
How many classrooms are needed by all student
'''

subject ={"python","java","C++","python","javascript","java","python","C","C++"}

# we are storing the list of subjects in a set as we need unique subject to get the count of number of classrooms
print(subject)
print("Number of classrooms needed :",len(subject))



#3 WAP to enter marks of 3 students from the user and store them in a dictionary. Start with an empty dict and add one by one. use Subject name as key and marks as value

"""
marks ={}


marks1 = float(input("Enter the marks of subject 1"))
marks.update({"phy":marks1})

marks2 = float(input("Enter the marks of subject 2"))
marks.update({"chem":marks2})

marks3 = float(input("Enter the marks of subject 3"))
marks.update({"bio":marks3})

print(marks)

"""

#4 create set value

values = {9,"9.0"}
print(values)

val ={
    ("float",9.0),
    ("int",9)
}

print(val)

print(type(val))

