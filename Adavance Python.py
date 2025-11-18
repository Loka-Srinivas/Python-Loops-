# # ADVANCED PYTHON:
    
# # Exception Handling:
# Error:
#    It is an interruption in our program which stops the flow of execution abruptly.
#    Types of errors:
       
# 1. Compile time error/syntax errors:
#     These  are the errors which occur during compiling a program.
      
#     EG: print("hello" world)
    
# 2. Exception/run-time errors:
    
#     These errors occur during execution/ run time interpretation of a program

# EG: print(10/0)   gives ZeroDivisionError
# list1=[1,2,3,4,5]
# print(list1[6])   

# In order to handle these exceptions so that the flow of execution of program 
# won't be interrupted we use a mechanism called exception handling. 

# For exception handling we use two main keywords: try and except.

# try:
# In try block we write the code which has the possibility of raising an exception.Exception

# except:
# In this block we write the code that should happen when an exception is occurred.

# We cannot write a try block without an except block.

# Syntax:
# try:
#     # block of code which may raise an exception.
    
# except:
#     # block of code to handle the exception.     
        
# try:        
#     num1=int(input("Enter a number:"))
#     num2=int(input("Enter another number:"))
#     # 
#     div=num1/num2
#     print("The division is:",div)
     
# except ZeroDivisionError:
#      print("Cannot divide a number by zero")
     
# print("Exception continued even after an exception occurred / handling")   

# # Handling Index Error:

# try:
#     list1=[1,2,3,4,5]
#     indVal=int(input("Enter the index val of the number:"))
#     print(list1[indVal])
# except IndexError:
#     print("Hightest index value availble is 4")    
    
# By default an except block witha specified error can only handle that one error. 
# If your program can raise multiple types of exceptions then your program might need multiple except blocks to handle those exceptions.

# except ValueError:
#      print("please provide interger value only")      

     
     
# TASK:

# list1=[2,3,4,5,'Lokanath',6,7,8]
# perform sum of the list and also handle the error with exception handling.

list1=[2,3,4,5,'Lokanath',6,7,8] 
sum1=0
for i in list1:
    sum+=i
    print("Sum")

 
        
           
     

        