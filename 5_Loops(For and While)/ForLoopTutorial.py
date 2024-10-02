#For loop

#It is used for sequential traversal.
#For traversing list , string and tuples etc
'''
num = [1,2,3,4,5] 

for val in num:
    print(val)
else:
    print("All values printed")




veg =["carrrt","Potatao","Brinjal","Lady Finger","Cucumber"]

for val in veg:
    print(val)
else:
    print("All values printed")

#use of else is mostly used with break statement

#print the elements of list using for loop

num_list =[1,2,5,3,4,5,6,7]
x=5
idx = 0
count =0
idx_list =[]
for val in num_list:
    if(val ==5):
        count +=1
        idx_list.append(idx)
    idx +=1

print(f"Entered number {x} found {count} times at below indexes \n",idx_list)


#Range function  in for loop

#range() - It returns a sequence of numbers, starting from 0 by default, and increment by 1
#and stops before a specified number

#range(start?, stop,step?)


for i in range(10): #only stop
    print(i)

for i in range(1,5): #start, stop
    print(i)

for i in range(0,10,2): #starts, stop and step
    print(i)

'''

n = int(input("Enter the number"))
for i in range(1,11):
    print(f"{n} * {i} =",n*i)

#pass statement

#pass is null statement that does nothing. It's used as placeholder for future code

for i in range(10):
    pass

print("Pass the loop")

#WAP to sum first n numbers

num = int(input("Enter the number"))
sum =0
for i in range(0,num+1):
    sum+=i
print(f"The sum of first {num} numbers =",sum)


#WAP to factorial of a given number

f_num = int(input("Enter the number to find its factorial"))
fact =1
for i in range(1,f_num+1):
    fact *=i
print(f"The factorial of {f_num} = ",fact)


