import pandas as pd
import random
import string
import os

# Pfad zum Verzeichnis, das möglicherweise nicht existiert
directory = 'data'

# Überprüfen Sie, ob das Verzeichnis existiert, und erstellen Sie es, wenn es nicht existiert
if not os.path.exists(directory):
    os.makedirs(directory)

# Function to generate random names
def generate_random_name():
    first_name = ''.join(random.choices(string.ascii_uppercase, k=1)) + \
                 ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 8)))
    last_name = ''.join(random.choices(string.ascii_uppercase, k=1)) + \
                ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 8)))
    return f"{first_name} {last_name}"

# Generate data for Students
students = pd.DataFrame({
    "student_id": range(1, 1501),
    "name": [generate_random_name() for _ in range(1500)],
    "major": random.choices(["Computer Science", "Physics", "Mathematics", "Biology", "Chemistry"], k=1500),
    "semester": random.choices(range(1, 9), k=1500)
})

# Generate data for Lecturers
lecturers = pd.DataFrame({
    "lecturer_id": range(1, 104),
    "name": [generate_random_name() for _ in range(103)],
    "department": random.choices(["Computer Science", "Physics", "Mathematics", "Biology", "Chemistry"], k=103)
})

# Generate data for Rooms
rooms = pd.DataFrame({
    "room_id": range(1, 51),
    "building": random.choices(["Building A", "Building B", "Building C"], k=50),
    "room_number": ['R' + str(i) for i in range(1, 51)]
})

# Generate data for Modules
modules = pd.DataFrame({
    "module_id": range(1, 76),
    "module_name": [f"Module {i}" for i in range(1, 76)],
    "description": [f"Description of Module {i}" for i in range(1, 76)]
})

# Generate data for Courses
courses = pd.DataFrame({
    "course_id": range(1, 126),
    "course_name": [f"Course {i}" for i in range(1, 126)],
    "lecturer_id": random.choices(range(1, 104), k=125),
    "room_id": random.choices(range(1, 51), k=125),
    "module_id": random.choices(range(1, 76), k=125),
    "ECTS": random.choices([3, 4, 6], k=125)
})

# Generate data for Grades
grades = pd.DataFrame({
    "grade_id": range(1, 31),
    "letter_grade": random.choices(["A", "B", "C", "D", "E", "F"], k=30),
    "numeric_grade": random.choices(range(1, 101), k=30)  # Grading scale 1-100
})

# Generate data for Enrollments
enrollments = pd.DataFrame({
    "enrollment_id": range(1, 3001),
    "student_id": random.choices(range(1, 1501), k=3000),
    "course_id": random.choices(range(1, 126), k=3000),
    "grade_id": random.choices(range(1, 31), k=3000),
    "attempt_number": random.choices(range(1, 4), k=3000),
    "semester": random.choices(["Winter 2023/2024", "Summer 2024"], k=3000)
})

# Saving to CSV files
students_file = "./data/students.csv"
lecturers_file = "./data/lecturers.csv"
rooms_file = "./data/rooms.csv"
modules_file = "./data/modules.csv"
courses_file = "./data/courses.csv"
grades_file = "./data/grades.csv"
enrollments_file = "./data/enrollments.csv"

students.to_csv(students_file, index=False)
lecturers.to_csv(lecturers_file, index=False)
rooms.to_csv(rooms_file, index=False)
modules.to_csv(modules_file, index=False)
courses.to_csv(courses_file, index=False)
grades.to_csv(grades_file, index=False)
enrollments.to_csv(enrollments_file, index=False)

students_file, lecturers_file, rooms_file, modules_file, courses_file, grades_file, enrollments_file