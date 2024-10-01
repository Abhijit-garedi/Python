# Open a file for writing
file = open("avi.txt", "w")
file.write("Hello, this is a test file.")
file.close()

# Open the file for reading
file = open("avi.txt", "r")
content = file.read()
print(content)
file.close()

# Append data to the file
file = open("avi.txt", "a")
file.write("\nThis is additional text.")
file.close()

# Read the updated file
file = open("avi.txt", "r")
updated_content = file.read()
print(updated_content)
file.close()
