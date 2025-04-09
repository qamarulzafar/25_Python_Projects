# Student Result Management System

# Project Description:

# A console-based Python application where the user can add, view, search, and update student records along with their marks. It helps manage results for a small class or lab.


student = []

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))
    grade = calculate_grade(marks)
    student.append({"name": name, "roll": roll, "marks": marks, "grade": grade})
    print("Student added successfully.")


def view_student():
    if not student:
        print("No Student Record Found.")
    else:
        for s in student:
            print(s)
    

def search_student():
    roll = input("Enter roll number: ")
    for s in student:
        if s["roll"] == roll:
            print(s)
            return
    print("Student not found.")


def update_marks():
    roll = input("Enter roll number: ")
    for s in student:
        if s["roll"] == roll:
            new_marks = float(input("Enter new marks: "))
            s["marks"] = new_marks
            s["grade"] = calculate_grade(new_marks)
            print("Marks updated successfully.")
            return
    print("Student not found.")


def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
    

def main():
    while True:
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_marks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



