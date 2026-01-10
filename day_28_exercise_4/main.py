import random
import string

word = input("Enter word: ")
choice = input("Code or Decode? ").lower()

def coding(word):
    if len(word) < 3:
        return word[::-1]
    else:
        r1 = ''.join(random.choice(string.ascii_letters) for _ in range(3))
        r2 = ''.join(random.choice(string.ascii_letters) for _ in range(3))
        return r1 + word[1:] + word[0] + r2

def decoding(word):
    if len(word) < 3:
        return word[::-1]
    else:
        word = word[3:-3]
        return word[-1] + word[:-1]

if choice == "code":
    print(coding(word))
else:
    print(decoding(word))
