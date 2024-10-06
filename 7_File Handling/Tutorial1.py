#File handling in python

# Types:

# 1.Text Files
# 2. Binary Files

#In memory files are stored in memory in form of bits


#Open a file

f= open("C:/Users/Lenovo/Documents/Python_for_Beginners/7_File Handling/demo.txt","r")
data = f.read()
#f.write("I'll love to learn DSA further and then create my own application in future")
print(data)
#print(type(data))
f.close()


#file get truncated in  w+ mode

# r+ == read and write and pointer is at start == no truncate
# w+ == read and write  -- truncate
# a+ read and write -- pointer at the end -- no truncate





# with Syntax

with open("C:/Users/Lenovo/Documents/Python_for_Beginners/7_File Handling/sample.txt", "w") as file_text:
    #data_txt = file_text.read()
    file_text.write("""You're learning Python
Python is a scripting language
I'll love to learn DSA further and then create my own application in future""")
    #print(data_txt)
    file_text.close()