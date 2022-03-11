# Old first class Student
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

# New calculate method middle grade for Student 
    def midgrade_stud(self):
        total_stud = 0
        calc_grade = 0
        for i in self.grades.values():
            total_stud += sum(i)
            calc_grade += len(i)
        mg_stud = round((total_stud / calc_grade), 1)
        return mg_stud

# New method compare students by the middle grade
    def __gt__(self, other):
        if not isinstance(other, Student):
            return
        return Student.midgrade_stud(self) > Student.midgrade_stud(other)

# Use __str__ method for Student
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {Student.midgrade_stud(self)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

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

# New calculate method middle rate for Lecturer 
    def midrate_lect(self):
        total_sum = 0
        calc_rate = 0
        for i in self.stud_rate.values():
            total_sum += sum(i)
            calc_rate += len(i)
        mr_lect = round((total_sum / calc_rate), 1)
        return mr_lect

# Use __str__ method for Lecturer
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {Lecturer.midrate_lect(self)}'

# New method compare lecturers by the middle rate
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return Lecturer.midrate_lect(self) < Lecturer.midrate_lect(other)

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

# Use __str__ method Reviewer
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# Block of tests

# test __str__ for some_reviewer
some_reviewer = Reviewer('Some', 'Buddy')
print(some_reviewer)
print('<>' * 50)

# test __str__ for some_lecturer
some_lecturer = Lecturer('Some', 'Bubby')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['PHP']
some_lecturer.courses_attached += ['CSS']
some_lecturer.stud_rate['Python'] = [9, 10, 10]
some_lecturer.stud_rate['PHP'] = [10, 10, 10]
some_lecturer.stud_rate['CSS'] = [10, 10, 10]
print(some_lecturer)
print('<>' * 50)

# test __str__ for some_student
some_student = Student('Ruoy', 'Eman', 'M')
some_student.courses_in_progress = ['Python', 'Git']
some_student.finished_courses = ['Введение в программирование']
some_student.grades['Python'] = [10, 10, 9, 10]
some_student.grades['Git'] = [10, 10, 10, 10]
print(some_student)
print('<>' * 50)

# test compare the students
# the first student
student_1 = Student('Ivan', 'Ivanov', 'M')
student_1.courses_in_progress = ['Python', 'Git', 'PHP']
student_1.finished_courses = ['Введение в программирование']
student_1.grades['Python'] = [10, 10, 9, 10]
student_1.grades['Git'] = [10, 10, 10, 10]
student_1.grades['PHP'] = [10, 10, 10, 9]
student_1.grades['Введение в программирование'] = [10, 10, 10, 9]
# the second student
student_2 = Student('Roman', 'Romanov', 'M')
student_2.courses_in_progress = ['Python', 'Git']
student_2.finished_courses = ['Введение в программирование']
student_2.grades['Python'] = [8, 9, 9, 10]
student_2.grades['Git'] = [10, 8, 10, 9] 
student_1.grades['Введение в программирование'] = [9, 8, 10, 9]
print(f'Is STUDENT  {student_1.surname}  {student_1.name} is better then  {student_2.surname}  {student_2.name}  ----  It is ', Student.midgrade_stud(student_1) > Student.midgrade_stud(student_2))
print(f'Because STUDENT {student_1.surname} have middle grade: {Student.midgrade_stud(student_1)} and {student_2.surname} have middle grade: {Student.midgrade_stud(student_2)}.')
print('<>' * 50)

# test compare the lecturers
# the first lecturer
lecturer_1 = Lecturer('Igor', 'Petrov')
lecturer_1.stud_rate['Python'] = [7, 10, 9, 7]
lecturer_1.stud_rate['Git'] = [10, 7, 10, 9]
lecturer_1.stud_rate['PHP'] = [7, 8, 10, 9]
# the second lecturer
lecturer_2 = Lecturer('Fedor', 'Sidorov')
lecturer_2.stud_rate['Python'] = [10, 10, 9, 10]
lecturer_2.stud_rate['Git'] = [10, 10, 10, 9]
lecturer_2.stud_rate['CSS'] = [10, 10, 10, 9]
print(f'Is LECTURER  {lecturer_2.surname}  {lecturer_2.name} is better then  {lecturer_1.surname}  {lecturer_1.name}  ----  It is ', Lecturer.midrate_lect(lecturer_1) < Lecturer.midrate_lect(lecturer_2))
print(f'LECTURER {lecturer_2.surname} have middle grade: {Lecturer.midrate_lect(lecturer_2)} and {lecturer_1.surname} have middle grade: {Lecturer.midrate_lect(lecturer_1)}.')
print('<>' * 50)