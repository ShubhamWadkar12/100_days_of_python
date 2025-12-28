day = int(input("Enter day's number: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _ if day !=4:
        print("Day is not Thursday")
    case _ if day !=5:
        print("Day is not Friday")
    case _:
        print("Invalid day")
        

""" char = input("Enter a character: ")

match char:
    case 'a':
        print("a is a vowel")
    case 'e':
        print("e is a vowel")
    case 'i':
        print("i is a vowel")
    case 'o':
        print("o is a vowel")
    case 'u':
        print("u is a vowel")
    case _:
        print("It is s consonant") """
