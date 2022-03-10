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
        for i in self.grades.values():
            total_stud += sum(i) / len(i)
        mg_stud = round((total_stud / len(self.grades)), 1)
        return mg_stud    

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
        self.mr_lect = 5

# New calculate method middle rate for Lecturer 
    def midrate_lect(self):
        total = 0
        for i in self.stud_rate.values():
            total += sum(i) / len(i)
        mr_lect = round((total / len(self.stud_rate)), 1)
        return mr_lect

# Use __str__ method for Lecturer
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {Lecturer.midrate_lect(self)}'

# New subclass from parent Mentor with initialisation
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

# New method put_rating
    def put_rating(self, lecturer, course, grade):
        if isinstance(lecturer, Student) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
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