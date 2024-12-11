import shutil

#name of source file and destination file
source_file = "source.txt"
destination_file = "destination.txt"

# copy stuffs form one to another 
shutil.copy(source_file, destination_file)

print(f"Content copied from {source_file} to {destination_file}.")
