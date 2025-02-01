# #complete constructor using static variable
# class car:
#     brand='AUDI' #STATIC VARIABLE
#     def __init__(self,model,year):
#         self.brand='audi'
#         self.model=model
#         self.year=year
#     def display(self):
#         print(f'The car detail as follows:')
# c1=car('a8',2022)
# c1.display()
# print(c1.brand)
# print(c1.model)
# print(c1.year)
# c2=car('a6',2020)
# c2.display()
# print(c2.brand)
# print(c2.model)
# print(c2.year)
# print(car.brand)
# car.brand='SKODA'
# print(car.brand)
# print(c2)

# ##POLYMORPHISM
# class cat:
#     def sound():
#         print('meow')


# #user input in ooops

# class student:
#     def __init__(self):
#         self.student_name='sandeep'
#         self.fathername='ravi'
#         self.village='nizamabad'
# class school(student):
#     def __init__(self):
#         super().__init__()
#         self.rollno=29
#         self.marks=list(map(int,input('enter the 5 subject marks with spaces:').split()))
#         self.percent=int(input('enter pass percentage'))
# class secondary(school):
#     stream='MPC' ##STATIC VARIABLE IT HELPS IN REDUCING CREATING OBJECT INSTANCE FOR EACH ATTRIBUTE
#     def __init__(self):
#         super().__init__()
#         self.stream="mpc"
#         self.secondary_marks=list(map(int,input('enter the 5 subject marks with spaces:').split()))
#         self.passout=2021
# class ug(secondary):
#     def __init__(self):
#         super().__init__()
#         self.branches=list(input('enter the streams:: ').split())
#         self.stream='ECE'
#         self.passout=2025
#     def display(self):
#         print(f'The details of student as follows: student name:{obj.student_name} \nfather name:{obj.fathername}')
# obj=ug()
# obj.display()
# print(obj.rollno)
# print(f'The marks you secured: {obj.marks}')
# obj.display()
# print(secondary.stream)
# print(f'The marks you secured: {obj.secondary_marks}')
# print(obj.percent)
# print(obj.passout)
# print(f'the available branches of ug {obj.branches}')

# #Method overriding

# class employee:
#     def __init__(self,name):##method is neglected by the interpreter
#         print(f'the constructor hello {name}')#It doesnt get executed because of multiple same methods
#     def __init__(self,age):##METHOD(CONSTRUCTOR) IS CONSIDERED
#         print(f'the employee  age {age}')## IT IS EXECUTED
# p1=employee(22)

# ##PASSING PARAMETERS INTO METHOD USING *ARG

# class Student:
#     name = 'sandeep'  # Default value for name (class level variable)

#     def __init__(self, *args):
#         # Use *args to handle variable positional arguments
#         if len(args) >= 2:  # Check if there are at least two arguments
#             self.name = args[0]  # The first argument will be the fullname
#             self.marks = args[1]  # The second argument will be marks
#         else:
#             self.name = "Unknown"  # Default if not enough arguments are passed
#             self.marks = 0  # Default marks
        
#         print(self)  # Printing the instance (this will print the object reference)
#         print('Adding new student in Database..')

# # Creating objects (instances) of the Student class
# s1 = Student('karan', 70)  # Pass two arguments for name and marks
# print(s1)  # Printing the s1 object (instance)
# print(s1.name)  # Accessing the name of the student
# print(s1.marks)  # Accessing the marks of the student

# s2 = Student('arjun', 60)  # Pass two arguments for name and marks
# print(s2.name)  # Accessing the name of the second student
# print(s2.marks)  # Accessing the marks of the second student

# s3 = Student()  # No arguments passed (defaults will be used)
# print(s3.name)  # Accessing the name of the third student
# print(s3.marks)  # Accessing the marks of the third student


# ###DESTRUCTOR

# class DestructorExample:
#     def __init__(self,name):
#         print(f'object {name} is created')
#         self.age=20
#     def __init__(self,name):
#         print(f'object {name} is destroyed')
# obj=DestructorExample('sample')
# del obj

# #MULTIPLE INHERITANCE

# class Bird:
#     def fly(self):
#         return('the bird can fly')
# class Animal:
#     def walk(self):
#         return('the Animal can walk')
# class Bat(Bird,Animal):
#     def dance(self):
#         return 'the bat can dance'
#     pass
# bat=Bat()
# print(bat.fly())
# print(bat.walk())
# print(bat.dance())
# a1=Animal()
# a1=bat
# print(a1.dance())

# class Student:
#     def details(self):
#         self.name='sandy'
#         self.age=20
# class Ug:
#     def ug_details(self):
#         self.stream='ece'
#         self.passout=2025
# class Pg(Student,Ug):
#     def pg_details(self):
#         self.duration=5
# ob=Pg()
# print(ob.duration)
# print(ob.name)

# #HIREACHIAL INHERITANCE

# parent class

# class shape:
#     def area(self):
#         return 'the area is:'
# #child class 1
# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2
# #child class 2
# class square(shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side*self.side
# obj=square(4)
# print(obj.area())

# ##MINI PROJECT

# class customers:
#     def __init__(self):
#         self.customer_id=list(map(int,input().split()))
#         self.customer_name=list(input('enter customer name:').split())
#         self.phone=list(map(int,input().split()))
#         #self.email=list(input('enter email of customers')
#         self.street=list(input('enter the street name:'))
#         self.city=list(input('enter the street name:'))
#         self.state=list(input('enter the street name:'))
#         self.zipcode=list(map(int,input('enter the street name:')))
# class orders(customers):
#     def __init__(self):
#         super().__init__()
#         self.orderid=list(map(int,input().split()))
#         self.orderstatus=list(input('enter order status:').split())
#         # self.orderdata=args[2]
#         self.required_date=list(map(int,input().split()))
#         self.shipped_date=list(map(int,input().split()))
#         # self.store_id=args[5]
#         # self.staff_id=args[6]
# class customers_order(orders):##USE DICTIONARY
#     def __init__(self):
#         super().__init__()
#         self.orderdetails=dict(zip(self.customer_id,self.orderid))

# c1=customers()
# c2=customers_order()

# print(c1.zipcode)

class customers:
    def __init__(self):
        self.customer_id = list(map(int, input("Enter customer IDs: ").split()))
        # self.customer_name = list(input('Enter customer names: ').split())
        # self.phone = list(map(int, input('Enter phone numbers: ').split()))
        # self.email = list(input('Enter email of customers: ').split())
        # self.street = list(input('Enter the street names: ').split())
        # self.city = list(input('Enter the city names: ').split())
        # self.state = list(input('Enter the state names: ').split())
        # self.zipcode = list(map(int, input('Enter the zip codes: ').split()))

class orders(customers):
    def __init__(self):
        super().__init__()
        self.orderid = list(map(int, input("Enter order IDs: ").split()))
        # self.orderstatus = list(input('Enter order statuses: ').split())
        self.required_date = list(map(int, input("Enter required dates (format: day month year): ").split()))
        self.shipped_date = list(map(int, input("Enter shipped dates (format: day month year): ").split()))
        # self.store_id = args[5]
        # self.staff_id = args[6]

class customers_order(orders):  # Use dictionary
    def __init__(self):
        super().__init__()
        if len(self.customer_id) == len(self.orderid):  # Ensure equal length before zipping
            self.orderdetails = dict(zip(self.customer_id, self.orderid))
        else:
            self.orderdetails = {}
            print("Warning: customer_id and orderid lists have different lengths.")
        self.orderstaus=dict(zip(self.required_date,self.shipped_date))

# c1 = customers()
c2 = customers_order()

# print("Zipcode list:", c2.zipcode)
print("Order Details customerid:orderid ", c2.orderdetails)
print(f'order status :{c2.orderstaus}')



