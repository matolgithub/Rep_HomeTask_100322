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
        total = 0
        for i in self.stud_rate.values():
            total += sum(i) / len(i)
        mr_lect = round((total / len(self.stud_rate)), 1)
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


# Fild tests

# New 2 instances class Student
student_1 = Student('Elena', 'Trofimova', 'F')
student_1.courses_in_progress = ['Python', 'Git']
student_1.finished_courses = ['Введение в программирование']
student_1.grades['Python'] = [10, 8, 9, 10]
student_1.grades['Git'] = [10, 7, 10, 10]

student_2 = Student('Dmitriy', 'Peskov', 'M')
student_2.courses_in_progress = ['Python', 'CSS']
student_2.finished_courses = ['PHP']
student_2.grades['Python'] = [10, 10, 9, 10]
student_2.grades['CSS'] = [10, 10, 10, 10]

# New 2 instances class Mentor
mentor_1 = Mentor('Semen', 'Shpakov')
mentor_1.courses_attached += ['Python']
mentor_1.courses_attached += ['PHP']
mentor_1.courses_attached += ['CSS']

mentor_2 = Mentor('Nicolay', 'Fedorov')
mentor_2.courses_attached += ['Python']
mentor_2.courses_attached += ['PHP']
mentor_2.courses_attached += ['CSS']

# New 2 instances class Lecturer
lecturer_1 = Lecturer('Nicolay', 'Fedorov')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['PHP']
lecturer_1.courses_attached += ['CSS']
lecturer_1.stud_rate['Python'] = [9, 10, 10]
lecturer_1.stud_rate['PHP'] = [10, 10, 10]
lecturer_1.stud_rate['CSS'] = [10, 10, 10]

lecturer_2 = Lecturer('Fedor', 'Sidorov')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['PHP']
lecturer_2.stud_rate['Python'] = [8, 10, 9, 10]
lecturer_2.stud_rate['PHP'] = [10, 7, 10, 9]

# New 2 instances class Reviewer
reviewer_1 = Reviewer('Semen', 'Shpakov')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['PHP']
reviewer_1.courses_attached += ['CSS']

reviewer_2 = Reviewer('Vladimir', 'Sokolov')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

# Test def midgrade_stud(self) for Student


# Test def __gt__(self, other) for Student
print(f'Is STUDENT  {student_1.surname}  {student_1.name} is better then  {student_2.surname}  {student_2.name}  ----  It is ', Student.midgrade_stud(student_1) > Student.midgrade_stud(student_2))
print(f'Because STUDENT {student_1.surname} have middle grade: {Student.midgrade_stud(student_1)} and {student_2.surname} have middle grade: {Student.midgrade_stud(student_2)}.')
print('<>' * 50)

# Test def __str__(self) for Student
print(student_1)
print('<>' * 50)
print(student_2)
print('<>' * 50)

# Test def lect_rating(self, lecturer, course, grade)


# Test def midrate_lect(self)


# Test def __str__(self) for Lecturer
print(lecturer_1)
print('<>' * 50)
print(lecturer_2)
print('<>' * 50)

# Test def __lt__(self, other) for Lecturer
print(f'Is LECTURER  {lecturer_2.surname}  {lecturer_2.name} is better then  {lecturer_1.surname}  {lecturer_1.name}  ----  It is ', Lecturer.midrate_lect(lecturer_1) < Lecturer.midrate_lect(lecturer_2))
print(f'LECTURER {lecturer_2.surname} have middle grade: {Lecturer.midrate_lect(lecturer_2)} and {lecturer_1.surname} have middle grade: {Lecturer.midrate_lect(lecturer_1)}.')
print('<>' * 50)

# Test def put_rating(self, student, course, grade) for Reviewer


# Test def __str__(self) for Reviewer
print(reviewer_1)
print('<>' * 50)
print(reviewer_2)
print('<>' * 50)