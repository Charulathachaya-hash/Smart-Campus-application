# =============================================
# SMART CAMPUS INFORMATION SYSTEM
# =============================================
# Features Included:
# 1. Student Registration and Grade Evaluation
# 2. Course Enrollment Management
# 3. Student Record Storage and Management
# 4. Searching and Sorting Student Data
# 5. Fee Calculation using Functions
# 6. File-Based Academic Record Management
# 7. Directory Scanning with Exception Handling
# 8. Student Performance Analytics using
#    NumPy, Pandas, and Matplotlib
# =============================================

import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =============================================
# GLOBAL STORAGE
# =============================================

students = []

DATA_FILE = "student_records.json"

# =============================================
# LOAD EXISTING RECORDS
# =============================================

def load_records():
    global students

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                students = json.load(file)
            except:
                students = []
    else:
        students = []

# =============================================
# SAVE RECORDS
# =============================================

def save_records():
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

# =============================================
# GRADE EVALUATION
# =============================================

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

# =============================================
# FEE CALCULATION
# =============================================

def calculate_fee(course_count):
    fee_per_course = 5000
    total_fee = course_count * fee_per_course

    if course_count >= 4:
        discount = total_fee * 0.10
    else:
        discount = 0

    final_fee = total_fee - discount
    return final_fee

# =============================================
# STUDENT REGISTRATION
# =============================================

def register_student():
    print("\n===== STUDENT REGISTRATION =====")

    reg_no = input("Enter Register Number: ")
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")

    num_subjects = int(input("Enter Number of Subjects: "))

    marks = []

    for i in range(num_subjects):
        mark = int(input(f"Enter mark for Subject {i+1}: "))
        marks.append(mark)

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)

    # Course Enrollment
    courses = []
    course_count = int(input("Enter Number of Courses to Enroll: "))

    for i in range(course_count):
        course = input(f"Enter Course {i+1}: ")
        courses.append(course)

    fee = calculate_fee(course_count)

    student = {
        "Register Number": reg_no,
        "Name": name,
        "Department": department,
        "Marks": marks,
        "Average": average,
        "Grade": grade,
        "Courses": courses,
        "Fee": fee
    }

    students.append(student)
    save_records()

    print("\nStudent Registered Successfully!")

# =============================================
# DISPLAY ALL STUDENTS
# =============================================

def display_students():
    print("\n===== STUDENT RECORDS =====")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\n--------------------------------")
        print("Register Number :", student["Register Number"])
        print("Name            :", student["Name"])
        print("Department      :", student["Department"])
        print("Marks           :", student["Marks"])
        print("Average         :", student["Average"])
        print("Grade           :", student["Grade"])
        print("Courses         :", ", ".join(student["Courses"]))
        print("Fee             :", student["Fee"])

# =============================================
# SEARCH STUDENT
# =============================================

def search_student():
    print("\n===== SEARCH STUDENT =====")

    reg_no = input("Enter Register Number to Search: ")

    found = False

    for student in students:
        if student["Register Number"] == reg_no:
            print("\nStudent Found!")
            print(student)
            found = True
            break

    if not found:
        print("Student Not Found.")

# =============================================
# SORT STUDENTS
# =============================================

def sort_students():
    print("\n===== SORT STUDENTS =====")
    print("1. Sort by Name")
    print("2. Sort by Average")

    choice = input("Enter Choice: ")

    if choice == "1":
        sorted_students = sorted(students, key=lambda x: x["Name"])

    elif choice == "2":
        sorted_students = sorted(
            students,
            key=lambda x: x["Average"],
            reverse=True
        )

    else:
        print("Invalid Choice")
        return

    for student in sorted_students:
        print(student["Name"], "-", student["Average"])

# =============================================
# DIRECTORY SCANNING WITH EXCEPTION HANDLING
# =============================================

def scan_directory():
    print("\n===== DIRECTORY SCANNING =====")

    path = input("Enter Directory Path: ")

    try:
        files = os.listdir(path)

        print("\nFiles and Folders:")
        for file in files:
            print(file)

    except FileNotFoundError:
        print("Error: Directory not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected Error:", e)

# =============================================
# PERFORMANCE ANALYTICS
# =============================================

def analytics():
    print("\n===== STUDENT PERFORMANCE ANALYTICS =====")

    if not students:
        print("No student data available.")
        return

    names = []
    averages = []

    for student in students:
        names.append(student["Name"])
        averages.append(student["Average"])

    # NumPy Analysis
    marks_array = np.array(averages)

    print("\n----- NUMPY ANALYSIS -----")
    print("Highest Average :", np.max(marks_array))
    print("Lowest Average  :", np.min(marks_array))
    print("Mean Average    :", np.mean(marks_array))

    # Pandas DataFrame
    df = pd.DataFrame({
        "Student": names,
        "Average": averages
    })

    print("\n----- PANDAS DATAFRAME -----")
    print(df)

    # Matplotlib Graph
    plt.figure(figsize=(8, 5))
    plt.bar(names, averages)
    plt.xlabel("Students")
    plt.ylabel("Average Marks")
    plt.title("Student Performance Analysis")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

# =============================================
# DELETE STUDENT RECORD
# =============================================

def delete_student():
    print("\n===== DELETE STUDENT =====")

    reg_no = input("Enter Register Number to Delete: ")

    for student in students:
        if student["Register Number"] == reg_no:
            students.remove(student)
            save_records()
            print("Student Record Deleted.")
            return

    print("Student Not Found.")

# =============================================
# MAIN MENU
# =============================================

def menu():
    load_records()

    while True:
        print("\n=================================")
        print(" SMART CAMPUS INFORMATION SYSTEM ")
        print("=================================")

        print("1. Register Student")
        print("2. Display Student Records")
        print("3. Search Student")
        print("4. Sort Students")
        print("5. Student Analytics")
        print("6. Directory Scan")
        print("7. Delete Student")
        print("8. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            sort_students()

        elif choice == "5":
            analytics()

        elif choice == "6":
            scan_directory()

        elif choice == "7":
            delete_student()

        elif choice == "8":
            print("Exiting Smart Campus System...")
            break

        else:
            print("Invalid Choice. Try Again.")

# =============================================
# PROGRAM START
# =============================================

menu()