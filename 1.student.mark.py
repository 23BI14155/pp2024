students = []
courses = []

def input_students():
    students_amount = int(input("Enter amount of students: "))
    for _ in range(students_amount):
        student_id = input("Enter student's ID: ")
        student_name = input("Enter student's name: ")
        student_dob = input("Enter student's date of birth (day/month/year): ")
        students.append({"id": student_id, "name": student_name, "dob": student_dob})

def list_students():
    print("Student list:")
    for student in students:
        print(f"Student's ID: {student['id']}, Student's name: {student['name']}, Student's date of birth: {student['dob']}")

def input_courses():
    numb_courses = int(input("Enter amount of courses: "))
    for _ in range(numb_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter courses name: ")
        courses.append({"ID": course_id, "name": course_name})

def list_courses():
    print("Course list:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")
        
while True:
    print("\nStudent Marks Management:")
    print("1. Input student information")
    print("2. Input course information")
    print("3. Display student list")
    print("4. Display course list")
    print("5. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        input_students()
    elif choice == "2":
        input_courses()
    elif choice == "3":
        list_students()
    elif choice == "4":
        list_courses()
    elif choice == "5":
        print("Exit")
        break