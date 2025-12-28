a = "!!!Shubham  !!!!    Shubham"
print(len(a))
print(a.upper())                                               #strings are immutable
print(a.lower())            
print(a.strip("!!!!!"))                                        #removes the specified characters from the beginning and the end        
print(a.replace("Shubham", "DevOps Engineer"))                 #replaces a substring with another substring                   
print(a.split(" "))                                            #splits the string into a list where each word is a list item

blogHeading = "string Methods in Python"
print(blogHeading.capitalize())                                #capitalizes the first character of the string

str1 = "Welcome to the world of Python"
print(len(str1))
print(len(str1.center(50)))                                    #centers the string in a field of given width
print(a.count("Shubham"))                                      #counts the occurrences of a substring in the string

str1 = "Welcome to the world of Python!!!"
print(str1.endswith("!!!"))                                    #checks if the string ends with the specified suffix


#Day13