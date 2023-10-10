# A Functions is a block of code which only runs when called.
# Functions without parameters.
def my_course_unit():
   print("Programming in Python")
my_course_unit()
def my_name():
    print("Pifua Milan") 
my_name() 
#calling the function so that it performs the particular task.
my_name()
my_course_unit()

# Function with parameter/arguments.
#Create a function that multiplies two numbers a and b where a = 3 and b = 10.
age = 24
def product_of_two_numbers(a, b):
    output = a * b
    print(f" the product of {a} and {b} is {output}")

product_of_two_numbers(3,10)
product_of_two_numbers(4, 20)    
product_of_two_numbers(5, 10)


#Create a function that returns your name and your age as arguments of the function.
def my_name_and_age(name,age):
    print(f"My name is {name} and I am {age} years old.")
my_name_and_age("Pifua Milan", 24)   

#Write a python function to find the maximum of three numbers.
# a=70, b=80 , c=63
def maximumValue(a,b,c):
    if a>b and a>c:
        print(f"{a} is greater than {b} and {c}")
    elif b>a and b>c:
        print(f"{b} is greater than {a} and {c}")  
    else:
        print(f"{c} is greater than {a} and {b}")
maximumValue(70, 80, 63)            


#Write a python function to sum all the numbers in a list.
#Sample list = [8, 2, 3, 0, 7]
def sum_of_all_numbers(f, g, h, i, j):
    output = f + g + h + i + j
    print(f" The sum of {f}, {g}, {h}, {i}, {j} is {output}.")
sum_of_all_numbers(8, 2, 3, 0, 7)    


#Write a python program a python program to reverse a string 1, 2, 3, 4, a, b, c, d
def my_string(str):
    str = "1, 2, 3, 4, a, b, c, d"
    reversed_string = (str)
    for n in reversed (str):
        print(n)
my_string("1, 2, 3, 4, a, b, c, d")        

#Write a python function to multiply all numbers in a list  [8, 2,3, -1, 7]
 
def multiplication_of_numbers(a, b, c, d, e):
    output = a * b * c * d * e
    print(f" The multiplication of {a} , {b }, {c}, {d} and {e} is {output}.")
multiplication_of_numbers(8, 2, 3, -1, 7)    

#Write a python program to print the even numbers from a given list [ 1, 2, 3, 4, 5, 6, 7, 8 ,9 ]
def even_numbers_in_list(k, l, m, n, o, p, q, r, s):
    even_list=[ l, n, p, r]
    print(even_list)
even_numbers_in_list(1, 2, 3, 4, 5, 6, 7, 8, 9)    


