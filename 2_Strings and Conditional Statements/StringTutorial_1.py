#String Tutorial

#String is a data type in Python and it stores sequence of characters


# Basic operations of strings

str1 ="India is my country "
str2 = "Delhi is its Capital"
str3 = "+91 is its country code"


# Concat operation
print(str1 + '\n' +str2 + '\n'+ str3)


#Length of String using len function

#--> Spaces are also counted in string
length_str = len(str1 + '\n' +str2 + '\n'+ str3)
print("Length of string : ",length_str)

# Indexing in Python Strings

index_str = "This is your Indexing Tutorial in Python"
print(index_str[0])


#Slicing in string

print(index_str[0:5])

#negative index

print(index_str[-20:-1])

# Few other string functions

str_new = "I am studying python from Spriseagain"


flag = False

#This logic will verify the string entered by the user.
'''
while(flag == False):
    str = input("Please enter the text required for verification")
    flag = str.lower().endswith("in")
     # lower is used here to convert all the upercase entry to lowercase for verfication
    if (flag == False):
        print("Entered string is incorrect")
    else:
        print("Verified")
        
'''

# Capitalize function

str = "i am teaching python basics"
str_new = str.capitalize() # Capitalize first character of the string  
print(str_new) #--> I am teaching python basics


#Replace function

str_rep = str.replace("python","javascript")
print(str_rep)

#Returns 1st occurance Index of  1st ocurrer

print(str.find('python')) # (first index)  -1 is a invalid index

print(str.count("i")) #Count of o










    



