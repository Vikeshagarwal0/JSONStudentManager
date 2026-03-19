import json
class StudentManager:
    def __init__(self):
        self.students = []
        self.load_student()

    def load_student(self):
        try:
            with open("students.json", "r") as f:
                self.students = json.load(f)
        except FileNotFoundError:
            self.students = []

    def save_student(self):
        with open("students.json", "w") as f:
            json.dump(self.students, f)

    def add_student(self, roll, name):
        for s in self.students:
            if s["roll"] == roll:
                return f"Student with roll {roll} already exists."
        new_student = {"roll": roll, "name": name}
        self.students.append(new_student)
        self.save_student()
        return "Student added successfully."

    def delete_student(self, roll):
        for s in self.students:
            if s["roll"] == roll:
                self.students.remove(s)
                self.save_student()
                return "Student deleted successfully."
        return f"Student with roll {roll} not found."

    def update_student(self, roll, name):
        for s in self.students:
            if s["roll"] == roll:
                s["name"] = name
                self.save_student()
                return "Student updated successfully."
        return f"Student with roll {roll} not found."

    def search_student(self, roll):
        for s in self.students:
            if s["roll"] == roll:
                print(f"ROLL\tNAME")
                return f"{s['roll']}\t{s['name']}"
        return f"Student with roll {roll} not found."
    
    def show_all_students(self):
        if not self.students:
            return "No students found."
        print(f"ROLL\tNAME")
        for s in self.students:
            print(f"{s['roll']}\t{s['name']}")

school = StudentManager()

while True:
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Show All Students")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            roll = int(input("Enter roll number: "))
            name = input("Enter name: ")
            s = school.add_student(roll, name)
            print(s)
        elif choice == 2:
            roll = int(input("Enter roll number: "))
            s = school.delete_student(roll)
            print(s)
        elif choice == 3:
            roll = int(input("Enter roll number: "))
            name = input("Enter name: ")
            s = school.update_student(roll, name)
            print(s)
        elif choice == 4:
            roll = int(input("Enter roll number: "))
            s = school.search_student(roll)
            print(s)
        elif choice == 5:
            s = school.show_all_students()
            print(s)
        elif choice == 6:
            print("Thank You for using the program.")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")