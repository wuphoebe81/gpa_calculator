import math

class conversion:

    def __init__(self, course_name, course_grade):
        self.course_name = course_name
        self.course_grade = course_grade

    @classmethod
    def conv(cls, course_grade):
        if course_grade.upper() == 'A':
            return 4.00
        elif course_grade.upper() == 'A+':
            return 4.30
        elif course_grade.upper() == 'A-':
            return 3.70
        elif course_grade.upper() == 'B':
            return 3.00
        elif course_grade.upper() == 'B+':
            return 3.30
        elif course_grade.upper() == 'B-':
            return 2.70
        elif course_grade.upper() == 'C':
            return 2.00
        elif course_grade.upper() == 'C+':
            return 2.30
        elif course_grade.upper() == 'C-':
            return 1.70
        elif course_grade.upper() == 'D':
            return 1.00
        elif course_grade.upper() == 'D+':
            return 1.3
        elif course_grade.upper() == 'D-':
            return 0.70
        elif course_grade.upper() == 'F':
            return 0.00
        else:
            raise TypeError

    def __str__(self):
        return f'Course {crs}: {course_name.upper()} | Grade: {course_grade.upper().strip()} | Point Quality: {conversion.conv(course_grade)}'

print('GPA Calculator')

num_courses = int(input('Number of Courses: '))

crs = 0
total_points = 0.0
table = []

while crs < num_courses:

    crs += 1
    global course_name
    global course_grade
    global info
    global gpa
    global record

    course_name = input(f'Enter Course {crs} Name: ')
    try:
        if len(course_name.strip()) == 0:
            raise TypeError
        pass
    except:
        print('Invalid course name. Please re-enter course name.')
        crs -= 1
        continue

    course_grade = input('Enter Course Letter Grade: ')
    try:
        points = float(conversion.conv(course_grade.strip()))
        total_points += float(conversion.conv(course_grade))
        info = conversion(f'{course_name}', f'{course_grade}')
        record = f'{conversion.__str__(info)}'
        print(f'{conversion.__str__(info)}')
        table.append(record)

    except:
        print('Invalid grade input. Please re-enter name and grade.')
        crs -= 1
        continue

print('\nCOURSES:')
for _ in table:
    print(f'{_}')

gpa = float(total_points / num_courses)
print(f'\nCalculated GPA: {round(gpa, 2)}')
input('...')