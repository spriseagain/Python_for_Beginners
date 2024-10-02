#For loop

#It is used for sequential traversal.
#For traversing list , string and tuples etc

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









