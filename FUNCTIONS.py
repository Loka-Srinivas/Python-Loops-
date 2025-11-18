# 07/08/2025
# FUNCTIONS IN PYTHON:-


def greet(): 
    print("Hello! Welcome to Python")

greet()


def print_numbers():
    for i in range(1, 6):
        print(i)

print_numbers()


def sum_10():
    total = 0
    for i in range(1, 11):
        total += i
    print("Sum =", total)

sum_10()


def print_even():
    for i in range(2, 21, 2):
        print(i)

print_even()


def quote():
    print("Believe in yourself!")

quote()


def add(a, b):
    print("Sum =", a + b)

add(10, 5)


def check_even(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")

check_even(7)


def square(n):
    print("Square =", n * n)

square(6)


def circle_area(r):
    pi = 3.14159
    print("Area =", pi * r * r)

circle_area(5)


def greet_name(name):
    print("Hello", name)

greet_name("Srinivas")

