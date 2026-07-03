import csv

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# Function to add student
def add_student():
    try:
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))

        with open("students.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([roll_no, name, marks])

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Enter numeric marks.")

# Function to generate results
def generate_results():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            with open("results.csv", "w", newline="") as result_file:
                writer = csv.writer(result_file)

                writer.writerow(["Roll No", "Name", "Marks", "Grade"])

                for row in reader:
                    roll_no = row[0]
                    name = row[1]
                    marks = float(row[2])

                    grade = calculate_grade(marks)

                    writer.writerow([roll_no, name, marks, grade])

        print("Results generated successfully!")
        print("Data saved in results.csv")

    except FileNotFoundError:
        print("students.csv file not found!")

    except ValueError:
        print("Invalid marks found in file!")

# Main Program
while True:
    print("\n===== STUDENT GRADE FILE MANAGER =====")
    print("1. Add Student")
    print("2. Generate Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        generate_results()
    elif choice == "3":
        print("Program Ended")
        break
    else:
        print("Invalid Choice!")