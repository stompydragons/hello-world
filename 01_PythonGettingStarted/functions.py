students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student['name'].title()) # Capitalises the first letter of the word
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)










def save_file(student):
    try:
        f = open('students.txt', 'a')
        f.write(student + "\n")
        f.close()
    except Exception:
        print('Could not save file')


def read_file():
    try:
        f = open('students.txt', 'r')
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print('Could not read file')


#Homework was to keep adding more students based on prompts
#
#add_student_flag = input('Do you want to enter a student? Type Y for yes, N for no: ')
#
# if add_student_flag == 'Y':
#     yes_no_flag = True
#     while yes_no_flag:
#         student_name = input('Enter student name: ')
#         student_id = input('Enter student ID: ')
#         add_student(student_name, student_id)
#         print_students_titlecase()
#         add_student_flag = input('Do you want to enter another student? Y for yes N for no: ')
#         if add_student_flag == 'Y':
#             yes_no_flag = True
#         else:
#             yes_no_flag = False

read_file()
print_students_titlecase()

student_name = input('Enter student name: ')
student_id = input('Enter student ID: ')

add_student(student_name, student_id)
save_file(student_name)
