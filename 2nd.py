# def display(data):
#     print(f"the area is {data}")
# def get_input():#getting inputs
#     received_length=input('length')
#     received_breadth=input('breadth')
#     return (received_breadth,received_length)
# def c_area(length,breadth):#calculation of area
#     return int(length)*int(breadth)
# def main():
#     (length,breadth)=get_input()
#     area=c_area(length,breadth)
#     display(area)
# main()


# Add 2 num find result show
# avg of 4 nums

# def display(data):#DISPLAY OF RESULT
#     print(f'the average of given numbers is {data}')
# def input_numbers():#INPUT OF NUMBERS
#     num1=int(input('enter num1:'))
#     num2=int(input('enter num2:'))
#     num3=int(input('enter num3:'))
#     num4=int(input('enter num4:'))
#     return (num1,num2,num3,num4)
# def total_sum(numb1,numb2,numb3,numb4):#CALCULATION OF SUM
#      sum2=(numb1+numb2+numb3+numb4)
#      return sum2
# def final_average(sum2):
#     return sum2/4
# def main():#MAIN FUNCTION
#     (num1,num2,num3,num4)=input_numbers()
#     sum2=total_sum(num1,num2,num3,num4)
#     average=final_average(sum2)
#     display(average)
# main()

##  BIGGEST AMONG 3

# def display(data):
#     print(f'The Greatest number is:{data}')
# def get_input():
#     num1=int(input('enter num1:'))
#     num2=int(input('enter num2:'))
#     num3=int(input('enter num3:'))
#     return(num1,num2,num3)
# def greatest(num1,num2,num3):#CALCULATION
#     if (num1>num2 and num1>num3):
#         return num1
#     elif(num2>num1 and num2>num3):
#         return num2
#     else:
#         return num3
# def main():
#     (num1,num2,num3)=get_input()
#     greatest_num=greatest(num1,num2,num3)
#     display(greatest_num)
#main()

#DISPLAY WITH THE VARIABLE NAME
#compare with for loop with dynamic variable input 

# import dis ##DISASSEMBLER
# def display(variable_name,data):#DISPLAY THE RESULT
#     print(f'The Greatest number is {variable_name}:{data}')
# def get_input():                #TAKE THE INPUTS
#     num1=int(input('enter num1:'))
#     num2=int(input('enter num2:'))
#     num3=int(input('enter num3:'))
#     return(num1,num2,num3)
# def greatest(num1,num2,num3):#COMPARISION OF ALL THE NUMBERS
#     if (num1>num2 and num1>num3):
#         return "num1", num1
#     elif(num2>num1 and num2>num3):
#         return "num2", num2
#     else:
#         return "num3",num3
# def main():                        #MAIN FUNCTION FOR ASSIGNING THE RETURNED VALUES
#     (num1,num2,num3)=get_input()
#     variable_name,greatest_num=greatest(num1,num2,num3)
#     display(variable_name,greatest_num)
#     dis.dis(display)
# main()


#DISASSEMBLER

# import dis
# def display(data):
#     print(f'the answer is:{data}')
# def get_input():
#     x=int(input('enter a number'))
#     y=int(input('enter a number'))
#     return (x,y)
# def sol(x,y):
#     return x*y,x/y
# def main():
#     (x,y)=get_input()
#     mul=sol(x,y)
#     display(mul)
#     dis.dis(display)
# main()

#PRIME OR NOT
# def is_prime_basic(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

#IS PRIME OR NOT 

# import math
# def is_prime(n):
#     if n<=1:
#         return False
#     if n==2:
#         return True
#     if n%2==0:
#         return False
#     for i in range(3,int(math.sqrt(n))+1,2):
#         if n%i==0:
#          return False
#     return True
# def main():
#     n=int(input('enter a number:'))
#     ans=is_prime(n)
#     print(ans)
# main()

#PRIME FOR THE GIVEN NUMBER RANGE
# import math
# #def display(a,b,data):
    
# def get_input():
#  while True:
#         a = int(input('Enter the starting number: '))
#         if a < 0:
#             print('Please enter a positive number for the starting number.')
#             continue  # Skip to the next iteration if input is invalid
#         b = int(input('Enter the ending number: '))
#         if a >= b:
#             print('Starting number must be smaller than the ending number.')
#         else:
#             return a, b
# def is_prime(n):
#     if n<=1:
#         return False
#     if n==2:
#         return True
#     if n%2==0:
#         return False
#     for i in range(3,int(math.sqrt(n))+1,2):
#         if n%i==0:
#          return False
#     return True
# def prime_numbers(a,b): #BY USING ARRAYS TO STORE THE VALUES
#     for i in range(a,b+1):
#         if is_prime(i):
#            print(f'the prime numbers in between{a} and {b} is:',i)
    
# def main():
#     a,b=get_input()
#     prime=prime_numbers(a,b)
#     #display(a,b,prime)
# main()

# import math
# def display(a,b,data):
#     print('the prime numbes between {a} and {b} is {data}')
# def get_input():
#     x=int(input('enter a '))