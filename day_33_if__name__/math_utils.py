def add(a, b):
    return a + b

print("This line runs always")

if __name__ == "__main__":
    print("This runs ONLY when file is run directly")
    print(add(2, 3))
