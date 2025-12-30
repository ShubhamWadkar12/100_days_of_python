for i in range(10):                                                       #for loop
    print(i+2)

for i in range(10):
    print(i+1)
    
name =  "Shubham"                                                           
for i in name:                                                              
    print(i)
    if(i== "u"):
        print("Something special detected")         
        
#Output                        
""" 
S
h
u
Something special detected
b
h
a
m """

colors = ["Red","Yellow","Orange","Blue"]
for color in colors:
    print(color)
    for i in color:
        print(i)
        
                                                                            #list iteration
greets = ["Hello", "World"]
for greet in greets:
    print(greet)
    for i in greet:
        print(i)
        

for k in range(1,12,3):                                                     #Increase by 3 each time
    print(k)       
