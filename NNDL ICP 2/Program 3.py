"""
Write a program, which reads heights (inches.) of customers into a list and convert these
heights to centimeters in a separate list using:
1) Nested Interactive loop.
2) List comprehensions
Example: L1: [150,155, 145, 148]
Output: [68.03, 70.3, 65.77, 67.13]
"""

# Function to convert inches to centimeters
def inches_to_centimeters(height):
    cms = height * 2.54
    return cms

# Nested Interactive Loop
def convert_heights_nested():
    # Input - Reading heights in inches into a list
    height_list = []
    x = int(input("Enter the number of customers: "))
    for i in range(x):
        height = float(input(f"Enter height (in inches) for customer {i+1}: "))
        height_list.append(height)

    # Conversion using a nested loop
    height_in_cms_nested = []
    for height in height_list:
        height_cms = inches_to_centimeters(height)
        height_in_cms_nested.append(height_cms)

    return height_in_cms_nested

# List Comprehensions
def convert_heights_list_comprehension():
    # Input - Reading heights in inches into a list
    y = int(input("Enter the number of customers: "))
    height_list = [float(input(f"Enter height (in inches) for customer {i+1}: ")) for i in range(y)]

    # Conversion using list comprehension
    height_in_cms_lc = [inches_to_centimeters(height) for height in height_list]

    return height_in_cms_lc

def start():
    print("Height conversion - Inches to Centimeters ")
    print("Option 1: Conversion using Nested Interactive Loop ")
    print("Option 2: Conversion using Listed Comprehension ")
    print("Option 3: Exit")
    while True:
        code = input("Select options (1 - 3): ")
        if code == '1':
            result_nested = convert_heights_nested()
            print("Converted Heights (in cm):", result_nested)

        elif code == '2':
            result_lc = convert_heights_list_comprehension()
            print("Converted Heights (in cm):", result_lc)

        elif code == '3':
            exit()

        else:
            print('\t \u274C Invalid input')

if __name__ == "__main__":
    start()
