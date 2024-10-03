import os

file_name = "example.txt"

with open(file_name, 'w') as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")

with open(file_name, 'a') as file:
    file.write("This is an appended line.\n")

with open(file_name, 'r') as file:
    content = file.read()
    print("File content after writing and appending:")
    print(content)

with open(file_name, 'r') as file:
    print("Reading the file line by line:")
    for line in file:
        print(line.strip())

with open(file_name, 'w') as file:
    file.write("This is a new content that overwrites the old content.\n")

