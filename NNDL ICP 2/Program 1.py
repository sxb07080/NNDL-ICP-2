"""
Write a program that takes two strings from the user: first_name, last_name. Pass these variables to
fullname function that should return the (full name).
o For example:
▪ First_name = “your first name”, last_name = “your last name”
▪ Full_name = “your full name”
o Write function named “string_alternative” that returns every other char in the full_name string.
Str = “Good evening”
Output: Go vnn
Note: You need to create a function named “string_alternative” for this program and call it from
main function.
"""

# Function concatenate first and last names
def fullname(first, last):
    name = first + ' ' +last
    return name

# Function to select alternate characters in a string
def string_alternative(name):
    modified_name = name[::2]
    return modified_name

if __name__ == '__main__':
    first_name = str(input("Enter first name: "))
    last_name = str(input("Enter last name: "))

    result = fullname(first_name, last_name)
    print("Fullname: ", result)

    output = string_alternative(result)
    print("String alternative: ", output)
