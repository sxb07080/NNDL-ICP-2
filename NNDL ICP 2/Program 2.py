"""
Write a python program to find the wordcount in a file (input.txt) for each line and then print the output.
o Finally store the output in output.txt file.
Example:
Input: a file includes two lines:
Python Course
Deep Learning Course
Output:
Python Course
Deep Learning Course
Word_Count:
Python: 1
Course: 2
Deep: 1
Learning: 1
"""

def count_file_stats(filename):
    try:
        # Open file in read mode
        with open(filename, 'r') as file:
            # Read all lines from the file into a list
            lines = file.readlines()

            # Open output file in write mode
            with open("output.txt", "w") as output_file:
                # Initialize a dictionary to store cumulative word counts
                cumulative_word_count = {}

                # Iterate through each line in the file
                for line in lines:
                    # Print each line
                    print(line.strip())

                    # Count occurrences of each word in the line
                    word_count = {}
                    words = line.split()
                    for word in words:
                        word_count[word] = word_count.get(word, 0) + 1
                        cumulative_word_count[word] = cumulative_word_count.get(word, 0) + 1

                    # Write the output to output.txt
                    output_file.write(line.strip() + "\n")
                    for word, count in word_count.items():
                        output_file.write(f"{word}: {count}\n")
                    output_file.write("\n")

                # Print cumulative word count at the end
                print("Word_Count:")
                for word, count in cumulative_word_count.items():
                    print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = input("Enter a filename: ")
    count_file_stats(filename)
