import datetime


class Person:
    def __init__(self, first_name, surname, dob, gender, email):
        self.first_name = first_name
        self.surname = surname
        self.dob = dob
        self.gender = gender
        self.email = email

    def get_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.dob.year
        print(f"{self.first_name} {self.surname} is {age} years old.")

    def get_details(self):
        print(f"First Name: {self.first_name}, Surname: {self.surname}, Dob: {self.dob}, Gender: {self.gender}, Email: {self.email}")


class Teacher(Person):
    def __init__(self, first_name, surname, dob, gender, email, staff_id, faculty):
        super().__init__(first_name, surname, dob, gender, email)
        self.staff_id = staff_id
        self.faculty = faculty

    def get_faculty(self):
        print(f"{self.first_name} is part of the {self.faculty} faculty.")

    def get_id(self):
        print(f"{self.first_name} {self.surname} with ID: {self.staff_id} is a teacher at this school.")

class Student(Person):
    def __init__(self, first_name, surname, dob, gender, email, student_id, year_co, house):
        super().__init__(first_name, surname, dob, gender, email)
        self.student_id = student_id
        self.year_co = year_co
        self.house = house

    def get_id(self):
        print(f"{self.first_name} {self.surname} with ID: {self.student_id} is a student at this school.")

class Parent(Person):
    def __init__(self, first_name, surname, dob, gender, email, child, phone_number):
        super().__init__(first_name, surname, dob, gender, email)
        self.child = child
        self.phone_number = phone_number

    def get_info(self):
        print(f"{self.first_name} {self.surname} is {self.child}'s parent and their phone number is {self.phone_number}")

teacher_dob = datetime.date(1990, 3, 5)
teacher = Teacher("Stephen", "Scott", teacher_dob, "Male", "stephen.scott32@det.nsw.edu.au", "SS5553", "Software Engineering")

student_dob = datetime.date(2010, 5, 9)
student = Student("Maksim", "Kniazev", student_dob, "Male", "maksim.kniazev@education.nsw.gov.au", "MK5554", 2022, "OSU")

parent_dob = datetime.date(1990, 4, 4)
parent = Parent("Alisha", "Kniazev", parent_dob, "Male", "alisha.kniazev@gmail.com", "Maksim Kniazev", 3030303033)

teacher.get_details()
teacher.get_age()
teacher.get_faculty()
teacher.get_id()

student.get_details()
student.get_age()
student.get_id()

parent.get_details()
parent.get_age()
parent.get_info()
