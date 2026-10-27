# Menu Driven Student Information Management
database = {}

def read_details():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    return roll, name, dept

def add_student():
    roll, name, dept = read_details()
    database[roll] = {"Name": name, "Department": dept}
    print("Student added successfully.")

def view_students():
    if len(database) == 0:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for roll, info in database.items():
        print("Roll No:", roll, "| Name:", info["Name"], "| Department:", info["Department"])

def search_student():
    roll = input("Enter Roll No to search: ")
    if roll in database:
        print(database[roll])
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    if roll in database:
        del database[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

def display_menu():
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
