# Introduction to Conditional Statements:

light = input("light : ").lower()

if (light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")


#Single line /Ternary operator

# <var> = val1 if <condition> else <val2>

food = input("food :")
eat = "Yes" if food.lower() == "cake" else "no"
print(eat)


#Clever if

age = int(input("age : "))
vote =("yes","no") [age > 18]
print(vote)