import os

#os.remove("C:/Users/Lenovo/Documents/Python_for_Beginners/7_File Handling/sample.txt")




with open("C:/Users/Lenovo/Documents/Python_for_Beginners/7_File Handling/practice.txt","w") as pfile:
    pfile.write("Hi Everyone, \nWe are learning File I/O\nusing Python\nI like programming in Python")
    #data =pfile.read()
    #print(data)
    pfile.close()
    f= open("C:/Users/Lenovo/Documents/Python_for_Beginners/7_File Handling/practice.txt","r")
    print(f.read())
    f.close()

#WAP that replaces all occurances of python with java in the above file

# f= open("C:/Users/Lenovo/Documents/Python_for_Beginners/7_File Handling/practice.txt","r")
# data = f.read()
# new_data = data.replace("Python","Java")
# print(new_data)

# with open("C:/Users/Lenovo/Documents/Python_for_Beginners/7_File Handling/practice.txt","w") as t:
#     t.write(new_data)
# f.close()
# t.close()  
word =input("Enter the word")


#defining the function to open a file at a given path, read the data
#From the data find the matching word 
def find_word(word):
        with open("C:/Users/Lenovo/Documents/Python_for_Beginners/7_File Handling/practice.txt","r") as f:
            data = f.read()
            if(data.find(word) !=-1):
                print("Entered word is found")
            else:
                print("Incorrect input")
        f.close()

find_word(word)

def checkline_word(word):
        data = True
        line_no =1
        list =[]
        with open("C:/Users/Lenovo/Documents/Python_for_Beginners/7_File Handling/practice.txt","r") as l:
            while data:
                data = l.readline()
                if(word in data):
                    print(list)
                    print(line_no)
                    return
                line_no+=1
        return -1
checkline_word(word)









