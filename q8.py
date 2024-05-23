# change OOP
class student:
    def __init__(self,name):
        self.name = name
    def get_student_name(self):
        return self.name
class student_collection:
    def __init__(self,course_name,

                 ):
        self.course_name = course_name
        self.student_list = []

    def add_student(self,student):
        self.student_list.append(student)

    def remove_student(self,student):
       self.student_list.remove(student)

    def get_student(self,student):
        self.student_list.get(student)

def get_student_name(self):
    return self.name

def sort_student(self,student):
        self.student_list.sort(key=get_student_name)
