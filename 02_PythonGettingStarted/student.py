students = []

class Student:

    school_name = 'Springfield Elementary'

    def __init__(self, name, last_name, student_id=999):
        self.name = name
        self.student_id = student_id
        self.last_name = last_name
        students.append(self)

    def __str__(self):
        return 'Student ' + self.name

    def get_name_capitalize(self):
        """
        Returns the student name
        :return: string - student name
        """
        return self.name.capitalize()

    def get_school_name(self):
        """
        Returns the class property school name
        :return: string - school name
        """
        return self.school_name