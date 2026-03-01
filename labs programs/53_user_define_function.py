#write a python program to create a user define functions and print the student name 
#and age 

def print_student_info(name,age):
    print(f"student name: {name}")
    print(f"student age: {age}")

student_name=input("enter the student name:")

student_age=input("enter the student age:")

print_student_info(student_name,student_age)