import csv
file_path = r"C:\Users\Ramkumar\OneDrive\Documents\XLSheet\Student_report.csv"

def add_student():
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    grade = input("Enter grade: ")
    
    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, marks, grade])
    print("Record added successfully!")

def view_students():
    try:
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            print("Student Records")
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("Error: No records found. The file has not been created yet.\n")
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    ch = input("Choice: ")
    
    if ch == '1':
        add_student()
    elif ch == '2':
        view_students()
    elif ch == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
