# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename: abc.java

# Prompt the user to input a filename and store it in the 'filename' variable
filename = input("Input the Filename: ")

# Split the 'filename' string into a list using the period (.) as a separator and store it in the 'f_extns' variable
f_extns = filename.split(".")

# Print the extension of the file, which is the last element in the 'f_extns' list
print("The extension of the file is : " + repr(f_extns[-1]))



# explaination of the programe:-

# At first the siad code prompts the user to input a filename and stores it in the variable "filename". It then uses the string method split() to split the value of "filename" by "."(dot) and assigns the result to the variable "f_extns".

# The code then uses the index -1 to access the last element of the list "f_extns" which is the file extension and prints the message "The extension of the file is : " followed by the last element.

# The repr() function returns a string containing a printable representation of an object.

# For example, if the user inputs "abc.txt" as the filename, the code will print "Th e extension of the file is : 'txt'"
