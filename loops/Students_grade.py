# A program to calculate the grade of a student based on marks entered
print("Enter your marks (0 to 100):")

while True:
    try:
        marks = float(input())

        if marks < 0 or marks > 100:
            print("Please enter a valid number between 0 and 100.")
        else:
            # Grading system 
            if marks >= 90:
                grade = 'A'
            elif marks >= 80:
                grade = 'B'
            elif marks >= 70:
                grade = 'C'
            elif marks >= 60:
                grade = 'D'
            else:
                grade = 'F'

            print(f"Your grade is: {grade}")
            break

    except ValueError:
        print("Invalid input. Please enter a number.")
