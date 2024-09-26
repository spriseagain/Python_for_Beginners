# Lists in Python

'''
Tuple is a built in data type in Python that stores set of values and is immutable just as string

It can store elements of different types( int, float, string etc)





-->strings in python are immutable


-->Tuples are immutable 

'''

marks1 =90.5
marks2 =91.25
marks3 =80.0
marks4 =73.0
marks5 =60.8

marks = (90.5, 91.25, 80.0, 73.0, 60.8) # defining the tuple --> paranthesis used instead of square brackets same as lists
print(marks)
print(type(marks))  #----> It'll give type as tuple.


print(len(marks))

#indexing
print(marks[0]) 

#slicing is same as string
print(marks[1:4])
print(marks[1:4:2])

'''


str ="hello"
print(str)
#str[0]="y" #TypeError: 'str' object does not support item assignment


'''
#Tuples is immutable same as string unlike list 

tup = (1)
tup1 = ("cup")

print(type(tup))

print(type(tup1))

#<class 'int'>
#<class 'str'>


tupl = (1,)
tupl1 = ("cup",)

print(type(tupl))

print(type(tupl1))

#<class 'tuple'>
#<class 'tuple'>

#Tuple to be defined appropraitely


'''
student = ["Suraj", "Jhon","Arjun", "Ram", "Shyam"]
print(student[0])
student[0]= "Sooraj"
student[4]="Arya"

print(student) #mutable

'''
#Methods in Tuples 


#List specific methods

#1.Append -- Add a new value at the end of the list




test_tup = (7,1,3,5,4)

#Mutating the list
test_tup_appnd =test_tup.append(4) 

#Sorting the list -- asc or desc

sort_asc = list.sort()
print(sort_asc)  #=== this will return none

list.sort(reverse = True)

print(list) # this will return the sorted list

str_list =["grapes","apple","chikoo","bananna"]

print(str_list.sort())
print(str_list)


#Reverse the list

str_list.reverse()
print(str_list)

