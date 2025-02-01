#array
# def main():
#     n=int(input('enter the size of array:'))
#     array=[]
#     for i in range(n):
#         ele=int(input(f"Enter element {i}: "))
#         array.append(ele)
#     print(array)
# main()
#ARRAY INBUILT
# def main():
#     n=int(input('enter the size of array:'))
#     array=[]
#     for i in range(n):
#         array.append(i)
#     print(array)
#main()
##LIST
# l1=[]
# print('empty list',l1)
# l2=[1,3,4,5,6,7]
# print('list with elements:',l2)
# #NESTED LIST
# l3=[1,2,[3,4,5]]
# print('the nested list:',l3)
# #accesing list
# print('element',l3[2][1])
# l4=list(range(-4,4))
# print('list created from range:',l4)
# l5=[0,1,2,3,4,5,6,7]
# print('list slicing from 1 to 6:',l5[1:7])
# l6=[10,20,30,40,50]
# print('element at index 2:',l6[2])
# l7=[10,[100,200,300,400],50]
# print('accessing sublist',l7[1])
# print('accessing ele from sublist',l7[1][1])
# print('accessing the last element',l7[2])

##SUM OF LIST
# def list_sum(total_sum,list):
#     for i in list:
#         total_sum +=i
#     return total_sum

# def get_input():
#     n=int(input('enter the size of list:'))
#     list=[]
#     for i in range(n):
#         ele=int(input(f'enter the element {i+1}'))
#         list.append(ele)
#     return list
# def main():
#     list=get_input()
#     total_sum=0
#     total_sum=list_sum(total_sum,list)
#     print(f'the total sum of elements: {total_sum}')
# main()

# def list_sum(total_sum, list):
#     for i in list:
#         total_sum += i
#     return total_sum

# def get_input():
#     n = int(input('Enter the size of the list: '))
#     list = []
#     for i in range(n):
#         ele = int(input(f'Enter element {i+1}: '))
#         list.append(ele)
#     return list

# def main():
#     list = get_input()
#     total_sum = 0
#     total_sum = list_sum(total_sum, list)
#     print(f'The total sum of elements: {total_sum}')

##MAXIMUM AND MINIMUM IN THE GIVEN LIST 

# main()
# def using_sort(list):
#     list.sort()
#     min=list[0]
#     max=list[-1]
#     return min,max

# def min_max(list):
#     min_value=list[0]
#     max_value=list[0]
#     for i in list:
#         if i<min_value:
#             min_value=i
#         if i>max_value:
#             max_value=i
#     return min_value,max_value

# def get_input():
#     size=int(input('enter the size of list:'))
#     list=[]
#     for i in range(size):
#         ele=int(input(f'enter the {i+1}th element'))
#         list.append(ele)
#     return list
# def main():
#     list=get_input()
#     min,max=min_max(list)
# #     minv,maxv=using_sort(list)
# #     print(f"the min value is {min},the max value is {max}")
# #     print(f"the min value is {minv},the max value is {maxv}")
# # main()   
#  
# def ispalindrome(word):
#     rev=word[::-1]
#     if rev==word:
#         return word

# def count_palindrome(sentence):
#     count=0
#     word=''
#     for char in sentence:
#         if char.isalnum():
#             word+=char
#         else:
#             if word:
#                 if ispalindrome(word.lower()):
#                     count+=1
#                 word=""
#     if len(word)>0 and ispalindrome(word.lower()):
#         count+=1
#     return count
# def main():
#     sentence=input('enter a sentence: ')
#     palindrome_count=count_palindrome(sentence)
#     print(f'the palindrome count is {palindrome_count} ')

# main()     


##DICTIONARIES

d1={}
print('empty dictionary:',d1)

d2={'moon':2,'sun':1}
print('the dictionary with key and values',d2)

d3={'food':{'corn':2,'eggs':3}}
print('nested dictionary:',d3)

d4=dict(name='ram',age=25)
print('alternative construction',d4)

d5=dict(zip(['sandeep','ramu','raju'],[1,3,4]))
print('the dictionary as follows',d5)

