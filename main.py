class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.courses_in_progress and 0 < grade < 11 and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_rating(self):
        all_grades = []
        for course in self.grades.values():
            for grade in course:
                all_grades.append(grade)
        return f'Средняя оценка за домашние задания: {sum(all_grades) / len(all_grades)}'

    def __str__(self):
       formattedprint = f'Имя: {self.name}\n' \
                        f'Фамилия: {self.surname}\n' \
                        f'{self.__average_rating()}\n' \
                        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                        f'Завершенные курсы: {", ".join(self.finished_courses)}'
       return formattedprint

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.__average_rating() < other.__average_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}

    def __average_rating(self):
        all_grades = []
        for course in self.grades.values():
            for grade in course:
                all_grades.append(grade)
        return f'Средняя оценка за лекции: {sum(all_grades) / len(all_grades)}'

    def __str__(self):
       formattedprint = f'Имя: {self.name}\n' \
                        f'Фамилия: {self.surname}\n' \
                        f'{self.__average_rating()}'
       return formattedprint

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.__average_rating() < other.__average_rating()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
       formattedprint = f'Имя : {self.name}\n' \
                        f'Фамилия: {self.surname}'
       return formattedprint

def average_hw_all(students_list, course_name):
    all_grades = []
    for student in students_list:
        for grade in student.grades[course_name]:
            all_grades.append(grade)
    return f'Средняя оценка за домашние задания по всем студентам в рамках курса "{course_name}": {sum(all_grades) / len(all_grades)}'

def average_lecturers_rating(lecturers_list, course_name):
    all_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            for grade in lecturer.grades[course_name]:
                all_grades.append(grade)
    return f'Средняя оценка за лекции всех лекторов в рамках курса "{course_name}": {sum(all_grades) / len(all_grades)}'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
student2 = Student('Имя2', 'Фамилия2', 'гендер')
student2.courses_in_progress += ['Python', 'Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 1)
cool_mentor.rate_hw(student2, 'Git', 2)
cool_mentor.rate_hw(student2, 'Python', 2)

print(best_student.grades)

lecturer1 = Lecturer('имя1', 'фамилия1')
lecturer1.courses_attached += ['Python', 'Git']
lecturer1.courses_in_progress += ['Python']
best_student.rate_lecturer(lecturer1, 'Python', 2)
best_student.rate_lecturer(lecturer1, 'Python', 10)
best_student.rate_lecturer(lecturer1, 'Git', 5)         #оценка не добавится, т.к. курс "Git" не "in_progress"
# print(lecturer1.__dict__)
# print(lecturer1.grades)

lecturer2 = Lecturer('имя2', 'фамилия2')
lecturer2.courses_attached += ['Python', 'Git']
lecturer2.courses_in_progress += ['Python', 'Git']
best_student.rate_lecturer(lecturer2, 'Python', 1)
best_student.rate_lecturer(lecturer2, 'Python', 5)
best_student.rate_lecturer(lecturer2, 'Git', 3)
student2.rate_lecturer(lecturer2, 'Git', 9)
# print(lecturer2.__dict__)
# print(lecturer2.grades)

print(cool_mentor)

print(lecturer1)
print('\n')
print(lecturer2)
print('\n')
print(best_student)
print(student2)
print('\n')
print(best_student > student2)
print('\n')
print(lecturer1 < lecturer2)
print('\n')

students_list_1 = [best_student, student2]
print(average_hw_all(students_list_1, 'Git'))

lecturers_list_1 = [lecturer1, lecturer2]
print(average_lecturers_rating(lecturers_list_1, 'Git'))