#Functions

#Block of statements that perform a specific task
'''
#Function definition

def func_name(param 1, param 2):
    certain operations/work

    return the value

## call the function

func_name(arg1, arg2) #function call

'''


#function definition
def Cal_sum(a,b): #parameters
    sum = a+b
    #print(sum)
    return sum

sum = Cal_sum(2,3) #function call; arguments
print(sum)


def Cal_avg(a,b,c):
    return (a+b+c)/3

avg =Cal_avg(2,4,6)
print(avg)






'''
#Functions in Python

1. Built in Function

2.User Defined Function

'''

#Built in Function
print("Hello")


#Default parameters

def Cal_prod(a=1,b=1):
    print(a*b)
    return a*b
Cal_prod()




#Practice

#WAP to print the length of a list(list is a parameter)


cities =["Delhi","Gurgaon","Mumbai","Badlapur","Pune","Chennai"]
num =[1,2,3,4,5]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(num)


# WAP to print the elements of a list in a single line

def print_list(list):
    for item in list:
        print(item, end = " ")

print_list(cities)
print()


def cal_fact(n):
    fact =1
    for i in range(1,n+1):
        fact*=i
    print(fact)
    return fact

cal_fact(5)

def conv_usd_to_inr():
    inr =0
    amount = float(input("Enter amount in USD"))
    inr = amount * 90.5
    return inr

conv_inr = conv_usd_to_inr()
print(conv_inr)

def even_odd(num):
    if(num %2 ==0):
        print(f"{num} is Even")
    elif(num % 2 !=0):
        print(f"{num} is  Odd")
    else:
        print("Incorrect input")

number =int(input("Enter the number"))

even_odd(number)


