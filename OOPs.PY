
class Student:
    name='sandeep'
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print(self)#s1(object)always pointing to self in constructor
        print('adding new student in Database..')

#object/instance
s1=Student('karan',70)
print(s1)#s1(object)always pointing to self in constructor
print(s1.name)
s2=Student('arjun',60)
print(s2.name)

#car
# class Car:
#     color='black'
#     brand='audi'
# car1=Car()
# print(car1.color)
# print(car1.brand)