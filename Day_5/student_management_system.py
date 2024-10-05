class Student:
    total_students = 0
    def __init__(self, name, age, s_id):
        self.name = name
        self.age = age
        self.id = s_id
        self.courses = []
        Student.total_students +=1


    def enrolling(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in the course {course}")

    def display_info(self):
        print(f"Name: {self.name}"
              f"\nAge: {self.age}"
              f"\nID: {self.id}")
        if len(self.courses) > 0:
            print(f"Courses: {self.courses}")

        else:
            print("This student is not enrolled in any course!")



class Course:
    total_courses = 0
    def __init__(self, course_name, course_code, course_tutor, max_student):
        self.course_name = course_name
        self.course_code = course_code
        self.course_tutor = course_tutor
        self.max_student = max_student
        self.enrolled_students = []
        Course.total_courses +=1


    def add_student(self, student):
        if len(self.enrolled_students) > self.max_student:
            self.enrolled_students.append(student)
            student.enrolling(self.course_name)

        else:
            print("This course is full!")


def main():
    students = []
    courses = []

    while True:

        print("\n===== Student Management System =====")
        print()
        print("1. Add Student")
        print("2. Create Course")
        print("3. Enroll Student in Course")
        print("4. Display Student Info")
        print("5. Exit")
        choice = int(input("Enter the choice you want: "))
        if choice == 1:
            name = input('Enter the name of a student: ')
            try:
                age = int(input("Enter the age of a student: "))
            except ValueError:
                print("Please, enter the age in integers!")
                continue
            s_id = input("Enter the ID of a student: ")

            student_adding = Student(name, age, s_id)
            students.append(student_adding)

        elif choice == 2:
            cname = input("Enter the name of a course: ")
            ccode = input("Enter the code of a course: ")
            ctutor = input("Enter the tutor of a course: ")
            try:
                cmax = int(input("Enter the maximum number of students in the course: "))
            except ValueError:
                print("Enter only numbers here!")
                continue

            course_adding = Course(cname, ccode, ctutor, cmax)
            courses.append(course_adding)

        elif choice == 3:
            student_id = input("Enter the ID of a student: ")
            course_id = input("Enter the ID of a course: ")
            found_student = None
            for student in students:
                if student.id == student.id:
                    found_student = student
                    break

            found_course = None
            for course in courses:
                if course.course_code == course_id:
                    found_course = course
                    break
            if found_student and found_course:
                found_course.add_student(found_student)

            else:
                print("Either student or course was not found!")

        elif choice == 4:
            student_id = input("Enter the ID of a student to display info: ")
            found_student = None
            for student in students:
                if student.id == student.id:
                    found_student = student
                    break

            if found_student:
                found_student.display_info()
            else:
                print("Student not found")

        elif choice == 5:
           print("Thank you for being with us!")
           break

        else:
            print("Please, choose only valid options!")



if __name__ == "__main__":
    main()



