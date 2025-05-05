# 1. return the lenght of the string 
name = input('''enter your name :-''')
print(len(name))

# 2. conver a string in a lower case
print(name.lower())

# 3. conver a string in a upper case
capital_name = input("enter your name in small letters :-")
print(capital_name.upper())

# 4. replace the string into another string
string = input("enter the name :-")
print(string.replace(string," noob"))

# 5. split a string into a substring
a = "Hello, World !"
b = a.split(",")
print(b)

# 6 startswith / endswith
sw = input("enter your string sw:-")
print(sw.startswith("ta"))
print(sw.endswith("sh"))