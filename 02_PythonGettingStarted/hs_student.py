from student import *

class HighSchoolStudent(Student):
    school_name = 'Springfield High School'

    def get_school_name(self):
        """
        Overrides the parent behaviour and does not tell you the school name!
        :return: string - not the school name
        """
        return 'This is a High School Student'

    def get_name_capitalize(self):
        """
        Extends the parent behaviour by appending '-hs' to the student name
        :return: string
        """
        original_value = super().get_name_capitalize()
        return original_value + '-hs'