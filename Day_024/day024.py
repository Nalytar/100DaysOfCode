# udemy Course - 100 Days of Code - Python

# Add a High Score to our Snake game of Day 21

# Open, Read, Write and Close files
# file = open("my_file.txt")
# contents = file.read()
#
# print(contents)
# file.close()  # Closing is important to free the resources

# different way of opening file, automatically closing the file
with open("my_file.txt") as file:
    content = file.read()
    print(content)

with open("my_file.txt", "a") as file:  # "w" creates the file we want to open for writing if it doesn't exist
    file.write("\nNew text.")

# Absolute FilePaths always starts from the origin, the root
# Example: /C/User/Projects

# Relative FilePaths starts from the current work directory
# Example: ./Projects, going on up would be ../Another_Folder
#           if we want to address a file in the current working directory, we can also use just the name
