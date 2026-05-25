students = []

while True:
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        marks = input("Enter student marks: ")

        student = {
            "name": name,
            "age": age,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for student in students:
                print(student)

    elif choice == "3":
        name = input("Enter student name to delete: ")

        found = False
        for student in students:
            if student["name"] == name:
                students.remove(student)
                found = True
                print("Student deleted successfully!")
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")