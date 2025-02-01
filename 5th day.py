##OOPS IN PYTHON
# class parent:
#     def __init__(self):
#         self.ram='7CM'

#     def display_parent(self):
#         a=5
#         b=7
#         c=a+b
#         print(f'This is the parent class{c}')
# class child(parent):
#     def __init__(self):
#         super().__init__()
#     def display_child(self):
#         print('This is the child class')
# obj=child()
# obj.display_parent()
# obj.display_child()
# print(obj.ram)

class student:
    def __init__(self):
        self.student_name='sandeep'
        self.fathername='ravi'
        self.village='nizamabad'
class school(student):
    def __init__(self):
        super().__init__()
        self.rollno=29
        self.marks=list(map(int,input('enter the 5 subject marks with spaces:').split()))
        self.percent=int(input('enter pass percentage'))
class secondary(school):
    stream='MPC' ##STATIC VARIABLE IT HELPS IN REDUCING CREATING OBJECT INSTANCE FOR EACH ATTRIBUTE
    def __init__(self):
        super().__init__()
        self.secondary_marks=list(map(int,input('enter the 5 subject marks with spaces:').split()))
        self.passout=2021
class ug(secondary):
    def __init__(self):
        super().__init__()
        self.branches=list(input('enter the streams:: ').split())
        self.stream='ECE'
        self.passout=2025
    def display(self):
        print(f'The details of student as follows: student name:{obj.student_name} \nfather name:{obj.fathername}')
obj=ug()
print(obj.fathername)
obj.display()
print(obj.rollno)
print(f'The marks you secured: {obj.marks}')
obj.display()
print(secondary.stream)
print(f'The marks you secured: {obj.secondary_marks}')
print(obj.percent)
print(obj.passout)
print(f'the available branches of ug {obj.branches}')


