# Old first class Student
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

# Use __str__ method for Student
    def __str__(self):
        return f''

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
some_lecturer.stud_rate['Python'] = [9, 8, 10]
some_lecturer.stud_rate['PHP'] = [9, 9, 9]
some_lecturer.stud_rate['CSS'] = [10, 10, 10]
print(some_lecturer)
print('<>' * 50)

# test __str__ for some_lecturer
