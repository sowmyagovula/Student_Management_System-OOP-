# defining class
class Student:
    def __init__(self, Roll_no, Name, marks):
        self.Roll_no = Roll_no
        self.Name = Name
        self.marks = marks

    def __str__(self):
        return f"Roll_no: {self.Roll_no} \nName: {self.Name} \nMarks: {self.marks}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, Roll_no, Name, marks):
        student = Student(Roll_no, Name, marks)
        self.students.append(student)
        print("Student added successfully")

    def display(self):
        if not self.students:
            print("No students available.\n")
        else:
            print("\nStudent List:")
            for student in self.students:
                print(student)

    def update(self, Roll_no, Name = None, marks = None):
        for student in self.students:
            if student.Roll_no == Roll_no:
                student.Name = Name               
                student.marks = marks
                print(f"Student with Roll No {Roll_no} updated successfully!\n")
                return
        print("Student not found.\n")

    def delete(self, Roll_no):
        for student in self.students:
            if student.Roll_no == Roll_no:
                self.students.remove(student)
                print(f"Student with Roll No {Roll_no} deleted successfully!\n")
                return
        print("Student not found.\n")


# Main function
def main():
    sms = StudentManagementSystem()

    while(True):
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            Roll_no = input("Enter Roll No: ")
            Name = input("Enter Name: ")
            marks = int(input("Enter Marks: "))

            sms.add_student(Roll_no, Name, marks)
                
        elif choice == '2':
            sms.display()

        elif choice == '3':
            Roll_no = input("Enter roll number to update: ")
            Name = input("Enter new name: ")
            marks = float(input("Enter new marks: "))
            sms.update(Roll_no, Name, marks)

        elif choice == '4':
            Roll_no = input("Enter roll number to delete: ")
            sms.delete(Roll_no)

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()




