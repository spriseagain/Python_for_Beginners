# Lists in Python

'''
List is a built in data type in Python that stores set of values

It can store elements of different types( int, float, string etc)



How Lists is different from Array?

In lists , we can have data of different data types in a single list 
while in Array will have data of same type.

-->strings in python are immutable 
-->Lists are mutable 

'''

marks1 =90.5
marks2 =91.25
marks3 =80.0
marks4 =73.0
marks5 =60.8

marks = [90.5, 91.25, 80.0, 73.0, 60.8] # defining the list of marks in  a list
print(marks)
print(type(marks))  #----> It'll give it as list.

print(len(marks))

#indexing
print(marks[0]) 

#slicing is same as string
print(marks[1:4])
print(marks[1:4:2])


#List is mutable while string is immutable 

str ="hello"
print(str)
#str[0]="y" #TypeError: 'str' object does not support item assignment

student = ["Suraj", "Jhon","Arjun", "Ram", "Shyam"]
print(student[0])
student[0]= "Sooraj"
student[4]="Arya"

print(student) #mutable


#Methods in Lists 

'''
List specific methods

1.Append -- Add a new value at the end of the list


'''

list = [2,1,3]

#Mutating the list
list_apnd =list.append(4) 

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


#Insert Method

num_list =['a','c','x','z','f','a','z']
num_list.insert(1,5) #(.insert(index,value))
print(num_list)

#Remove method  -- Removes the first occurence of the given element

num_list.remove('z')
print(num_list) 

#POP method -- removes the element at the given index

num_list.pop(5)

print(num_list)











