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

str1 = "Let us start learning DevOps"                          
print(str1.find("us"))                                         # finds the first occurrence of the specified substring

str1 = "Welcome1"
print(str1.isalpha())                                          #checks if all characters in the string are alphabetic

str1 = "hello world"
print(str1.islower())                                          #checks if all characters in the string are lowercase

str2 = "   "
print(str2.isspace())                                          #checks if all characters in the string are whitespace

str2 = "HELLO WORLD"
print(str2.startswith("HELLO"))                                #checks if the string starts with the specified prefix

str2 = "HELLO WORLD"
print(str2.swapcase())                                         #swaps the case of each character in the string

