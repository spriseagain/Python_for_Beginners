#Loops are used to repeat instruction

#For traversing using indexes
"""

#intitalization
count =1

#check condition
while(count <=5):
    print(count)
    #increment
    count +=1

#we can also print the loop in reverse order as well

i=100

while(i>0):
    print("Logic",i)
    i-=1
print("Loop Completed",i)



## We should always 
# check for infinite loops 
# in our programming language


#Print table of a number n

n = int(input("Enter the number to print its table"))
i=1
while(i<=20):
    print(f"{n} * {i} =",n*i)
    i+=1

print("Table is printed for",n)




#Print the elemets of list using while loop

student = [1,"Sitara","Bucks",2,4,16,256,289]

print(student)
len_student = len(student)

# Logic to Traverse individual elements in a list
print("Length of string :- ",len_student)
idx=0
while(idx<len_student):
    print(student[idx])
    idx+=1
print("Entire list is printed")

"""

#Search for a number x in a given tuple using while loop

"""tup_heroes = (1,"Jhon",2,1,1,"Thor",3,"Capt. America",4,5,"End of Tuple")

# we can't sort a tuple

print(tup_heroes)
x = int(input("Entered the value to be searched in the given tuple"))
len_tup_heroes = len(tup_heroes)

print(len_tup_heroes)
idx =0
index_list =[]
count =0

while(idx < len_tup_heroes):
    if((tup_heroes[idx]) == (x)):
        index_list.append(idx)
        count +=1
    idx +=1

if(count>0):
    print(f"Enter value {x} is present {count} times at below mentioned indexes \n ",index_list) 
else:
    print("Value entered is missing")


tup_heroes = (1, "Jhon", 2, 1, 1, "Thor", 3, "Capt. America", 4, 5, "End of Tuple")

# Print the original tuple
print(tup_heroes)

# Get the value to be searched in the given tuple
x = input("Enter the string value to be searched in the given tuple: ")

# Determine if input is an integer or string
if x.isdigit():
    x = int(x)  # Convert to integer if it's a digit
    
# Get the length of the tuple
len_tup_heroes = len(tup_heroes)

# Initialize variables
idx = 0
index_list = []
count = 0

# Loop through the tuple to find the value
while idx < len_tup_heroes:
    if tup_heroes[idx] == x:
        index_list.append(idx)
        count += 1
    idx += 1

# Output the results
if count > 0:
    print(f"The entered value '{x}' is present {count} times at the following indexes:\n", index_list) 
else:
    print("The value entered is missing.")

"""

# Use of break and continue


#find factorial of first n numbers

num = int(input("Enter the number"))
i=1
idx =1
fact =1
while(i<=num):
    for i in range(1,i+1):
        fact*=i
    print(f"Fact of {i}  =",fact)

    i+=1
    fact =1

print("Task completed")


    
    

