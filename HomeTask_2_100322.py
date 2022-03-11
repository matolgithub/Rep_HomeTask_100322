# Old first class Student
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # New method lect_rating with the grade control
    def lect_rating(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if 0 < grade <= 10: 
                if course in lecturer.stud_rate:
                    lecturer.stud_rate[course] += [grade]
                else:
                    lecturer.stud_rate[course] = [grade]
            else:
                print('Wrong grade, must be 1-10!')
        else:
            print("It's wrong!")

# Old second class Mentor now without the method rate_hw
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
# New subclass from parent Mentor with initialisation
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.stud_rate = {}

# New subclass from parent Mentor with initialisation
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

# New method put_rating
    def put_rating(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "It's Mistake!"

# Block of tests

# Earlier tested
'''
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
cool_reviewer.put_rating(best_student, 'Python', 10)
cool_reviewer.put_rating(best_student, 'Python', 10)
cool_reviewer.put_rating(best_student, 'Python', 10)
 
print(best_student.grades)
print(best_student.name, best_student.surname, best_student.gender)
print(best_student.courses_in_progress, best_student.finished_courses)
print(cool_reviewer.name, cool_reviewer.surname, cool_reviewer.courses_attached)
'''
# New test
student_1 = Student('Ivan', 'Ivanov', 'M')
student_1.courses_in_progress += ['HTML + CSS']
lecturer_1 = Lecturer('Karl', 'Karlovich')
lecturer_1.courses_attached += ['HTML + CSS']
student_1.lect_rating(lecturer_1, 'HTML', 7)
student_1.lect_rating(lecturer_1, 'HTML + CSS', 22)
student_1.lect_rating(lecturer_1, 'HTML + CSS', 10)
print(f'Student {student_1.name} {student_1.surname} put to lecturer {lecturer_1.name} {lecturer_1.surname} marks {lecturer_1.stud_rate}')