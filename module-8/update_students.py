import json

# Function to print student list
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Load the original JSON data
with open("students.json", "r") as file:
    students = json.load(file)

# Notify and print original list
print("Original Student List:\n")
print_students(students)
print("\n")

# Append your info
new_student = {
    "F_Name": "Crystal",
    "L_Name": "Long",
    "Student_ID": 21396883,
    "Email": "crylong@my365.bellevue.edu"
}
students.append(new_student)

# Notify and print updated list
print("Updated Student List:\n")
print_students(students)
print("\n")

# Write updated list back to file
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

# Final confirmation
print("The students.json file has been updated.")
