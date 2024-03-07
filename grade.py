class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def enroll(self, course):
        self.courses[course.course_id] = None

    def assign_grade(self, course, letter_grade):
        if course.course_id in self.courses:
            self.courses[course.course_id] = letter_grade
        else:
            print(f"{self.name} is not enrolled in {course.name}")

    def calculate_gpa(self):
        total_points = 0
        total_credits = 0
        for course_id, letter_grade in self.courses.items():
            if letter_grade:
                course = courses[course_id]
                grade_points = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
                total_points += grade_points.get(letter_grade.upper(), 0) * course.credits
                total_credits += course.credits
        return total_points / total_credits if total_credits else 0

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

# Initialize empty dictionary to store courses
courses = {}

# Example usage:
# Take inputs for students and courses
num_students = int(input("Enter the number of students: "))
students = {}
for i in range(num_students):
    student_id = int(input(f"Enter student {i+1}'s ID: "))
    student_name = input(f"Enter student {i+1}'s name: ")
    students[student_id] = Student(student_id, student_name)

num_courses = int(input("Enter the number of courses: "))
for i in range(num_courses):
    course_id = int(input(f"Enter course {i+1}'s ID: "))
    course_name = input(f"Enter course {i+1}'s name: ")
    course_credits = int(input(f"Enter course {i+1}'s credits: "))
    courses[course_id] = Course(course_id, course_name, course_credits)

# Enroll students in courses
for student_id, student in students.items():
    print(f"\nEnrolling courses for {student.name}:")
    for course_id, course in courses.items():
        enroll_course = input(f"Do you want to enroll {student.name} in {course.name}? (yes/no): ").lower()
        if enroll_course == 'yes':
            student.enroll(course)

# Assign grades
for student_id, student in students.items():
    print(f"\nAssigning grades for {student.name}:")
    for course_id, course in courses.items():
        if course_id in student.courses:
            grade = input(f"Enter grade for {student.name} in {course.name} (A/B/C/D/F): ").upper()
            student.assign_grade(course, grade)

# Calculate GPA for each student
print("\nGPA Calculation:")
for student_id, student in students.items():
    print(f"{student.name}'s GPA: {student.calculate_gpa()}")
