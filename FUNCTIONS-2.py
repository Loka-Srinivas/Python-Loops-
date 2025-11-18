# 08/08/2025
# FUNCTIONS IN PYTHON:-


# Tasks on return Statement & Return Value:-

def cube(n):
    return n ** 3

print(cube(3))


def average(a, b):
    return (a + b) / 2

print(average(10, 20))


def square_and_root(n):
    return n ** 2, n ** 0.5

print(square_and_root(16))


def is_odd(n):
    return n % 2 != 0

print(is_odd(7))


def sum_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

print(sum_digits(1234))

# Tasks on Functions with Default Parameters:-


def greet(name='Guest'):
    return "Hello, " + name + "!"

print(greet())
print(greet("Srinivas"))


def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(2, 3))


def total_bill(item='Sandwich', quantity=1, price=50):
    return quantity * price

print(total_bill())
print(total_bill("Pizza", 2, 150))


def employee_info(name, age=30, department='HR'):
    return f"Name: {name}, Age: {age}, Department: {department}"

print(employee_info("Ravi"))
print(employee_info("Teja", 25, "IT"))


def circle_area(radius=1):
    return 3.14 * radius * radius

print(circle_area())
print(circle_area(5))


# Tasks on Loops with Return:-

def sum_even(n):
    total = 0
    for i in range(2, n+1, 2):
        total += i
    return total

print(sum_even(10))

def largest(numbers):
    return max(numbers)

print(largest([2, 8, 5, 12, 7]))


# Tasks with Multiple Return Values:-


def min_max(numbers):
    return min(numbers), max(numbers)

print(min_max([4, 2, 9, 1, 7]))


def student_summary(name, marks):
    total = sum(marks)
    avg = total / len(marks)
    return name, total, avg

print(student_summary("Ravi", [80, 90, 85]))


# Logical Task:-

def calculate(num1, num2, operator='+'):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2

print(calculate(10, 5))        # default +
print(calculate(10, 5, '-'))
print(calculate(10, 5, '*'))
print(calculate(10, 5, '/'))



print=[120,250,300,150,200]
total=0
for price in print:
    total=total+price
print("total sum of prices:", total)