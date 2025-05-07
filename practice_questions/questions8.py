# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename: abc.java

# Prompt the user to input a filename and store it in the 'filename' variable
filename = input("Input the Filename: ")

# Split the 'filename' string into a list using the period (.) as a separator and store it in the 'f_extns' variable
f_extns = filename.split(".")

# Print the extension of the file, which is the last element in the 'f_extns' list
print("The extension of the file is : " + repr(f_extns[-1]))
