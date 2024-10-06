#Read a file and check the number of even and odd numbers in the file seperated by commas


with open("C:/Users/Lenovo/Documents/Python_for_Beginners/7_File Handling/prac.txt","r") as f:
    data = f.read()
    print(data)
    #num =""
    even = []
    odd =[]
    even_count =0
    odd_count =0
    num =data.split(",")
    for item in num:
        if(item ==""):
            continue
        else:
            if(int(item) %2 ==0):
                even_count+=1
                even.append(item)
            else:
                odd_count+=1
                odd.append(item)
    
    print("Even count",even_count)
    print("Even List",even)
    print("Odd count",odd_count)
    print("Odd List",odd)




    # for i in range(len(data)):
    #     if(data[i]==","):
    #         print(num)
    #         # n = int(num)
    #         # num_list.append(n)
    #         num =""
    #     else:
    #         num +=data[i]




