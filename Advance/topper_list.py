# Student marks using dictionary
students = {"Ram": 85, "Shyam": 90, "Gita": 78, "Hari": 90}

topper = max(students, key=students.get)
print("Topper:", topper, "-", students[topper])

marks_list = list(students.values())
print("All Marks:", marks_list)

unique_marks = set(marks_list)
print("Unique Marks:", unique_marks)

sorted_marks = sorted(unique_marks)
print("Sorted Marks:", sorted_marks)
