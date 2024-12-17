class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DOB: {self.dob}"

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class Input_List:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        students_amount = int(input("Enter number of students: "))
        for _ in range(students_amount):
            student_id = input("Enter student's ID: ")
            student_name = input("Enter student's name: ")
            student_dob = input("Enter student's date of birth (day/month/year): ")
            self.students.append(Student(student_id, student_name, student_dob))

    def list_students(self):
        print("Student List:")
        for student in self.students:
            print(student)

    def input_courses(self):
        numb_courses = int(input("Enter number of courses: "))
        for _ in range(numb_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            self.courses.append(Course(course_id, course_name))

    def list_courses(self):
        print("Course List:")
        for course in self.courses:
            print(course)


def main():
    Input_List = Input_List()

    while True:
        print("\nStudent Marks Management:")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Display student list")
        print("4. Display course list")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            Input_List.input_students()
        elif choice == "2":
            Input_List.input_courses()
        elif choice == "3":
            Input_List.list_students()
        elif choice == "4":
            Input_List.list_courses()
        elif choice == "5":
            print("Exit")
            break

if __name__ == "__main__":
    main()