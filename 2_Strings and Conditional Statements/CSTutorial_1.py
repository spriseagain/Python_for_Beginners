#Conditional Statements

"""

if (condition):
    body
elif (condition):
    body
else:
    Body
"""

age =int(input("Enter your age"))
if (age>= 18):
    print("Eligible to vote")
else:
    print("Ineligible to vote")

# Grade based on Marks

marks = int(input("Enter your marks"))

if (marks>=90):
    print("Grade : A")
elif (marks <90 and marks >=80):
    print("Grade : B")
elif (marks <80 and marks >=70):
    print("Grade : C")
elif (marks <70 and marks >=50):
    print("Grade : D")
else:
    print("Grade not assigned")

