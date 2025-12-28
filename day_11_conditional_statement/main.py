a = int(input("Enter your age: "))
print("Your age is: " ,a)
 
#Conditional Operators: >, <, >=, <=, ==, !=

 #If-Else Statement
if a>18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
#If-Elif-Else Statement
if a<0 :
    print("The number is negative")
elif a==0:
    print("The number is 0")
else:
    print("The number is positive")
    
b = int(input("Enter your marks"))
if b >= 90:
    print("A")
elif b >=75:
    print("B")
elif b >=50:
    print("C")
else:
    print("Fail")
