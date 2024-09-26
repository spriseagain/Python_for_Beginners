# Set data structure in Python

"""
It's a collection of unordered immutable elements

"""

collection = {5,4,1,2,3,6,8,8,9,9}
print(collection) 

#it's unordered
print(type(collection))

print(len(collection)) #it'll ignore duplicate values

#create empty set

eset ={} #this will create empty dictionary

empty_set = set() #creates empty set

print(type(empty_set))


#Set Methods

# set.add

empty_set.add(1)
empty_set.add(2)
empty_set.add(3)
empty_set.add(2)

print(empty_set)


#set.remove

empty_set.remove(2)

print(empty_set)

print(len(empty_set))


#set.clear

empty_set.clear()
print(empty_set)


#set.pop

print(collection.pop())
print(collection.pop())


#union and intersection methods

#union -- gives union of two set combining the unqiue values

#intersection -- gives intersection of unique value

collect_1 ={23,23,42,1,3,5,3,2,5,4,6,7}
collect_2 ={1,2,3,4,5}

print(collect_1.union(collect_2))

print(collect_1.intersection(collect_2))








#





