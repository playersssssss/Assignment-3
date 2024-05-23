name= ['a','b','c','d']

student1 ={'Hello':'a'}
student2  = {'Hello':'b'}
student3 = {'Hello':'c'}
student4 = {'Hello':'d'}
students = [student1,student2,student3,student4]

def return_name(student):
    return student['name']
students.sort(key = return_name)