#Recursion

#When a function calls itself repeatedly

#prints n to 1 backwards

def fact(n):
    sum=1
    if(n==0):
        return 1
    print(n)
    #print("end")
    return n*fact(n-1)
    
result = fact(5)
print(result)


#Write a recursive function to calculate the sum of first n natural number

# sum = n(n-1)/2

def sum(n):
    if(n==0):
        return 0
    else:
         return n+sum(n-1)

result = sum(6)
print(result)


#print all elements in a list

list =[1,2,3,4,5]

def p_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    p_list(list,idx+1)


p_list([1,2,3,8,23,43])