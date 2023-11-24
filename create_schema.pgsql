DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS modules;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS lecturers;
DROP TABLE IF EXISTS students;

CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    major VARCHAR(100),
    semester INTEGER
);

CREATE TABLE Lecturers (
    lecturer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);

CREATE TABLE Rooms (
    room_id SERIAL PRIMARY KEY,
    building VARCHAR(100),
    room_number VARCHAR(100)
);

CREATE TABLE Modules (
    module_id SERIAL PRIMARY KEY,
    module_name VARCHAR(100),
    description TEXT
);

CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100),
    lecturer_id INTEGER REFERENCES Lecturers(lecturer_id),
    room_id INTEGER REFERENCES Rooms(room_id),
    module_id INTEGER REFERENCES Modules(module_id),
    ECTS INTEGER
);

CREATE TABLE Grades (
    grade_id SERIAL PRIMARY KEY,
    letter_grade VARCHAR(5),
    numeric_grade FLOAT
);

CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES Students(student_id),
    course_id INTEGER REFERENCES Courses(course_id),
    grade_id INTEGER REFERENCES Grades(grade_id),
    attempt_number INTEGER,
    semester VARCHAR(20) NOT NULL
);
