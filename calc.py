import math
from sympy import symbols, Eq, solve
#an external module to deal with symbols in mathematics for linear eqns

def add(x, y):  #add function
    return x + y

def subtract(x, y): #subtraction function
    return x - y

def multiply(x, y): #multiply function
    return x * y

def divide(x, y):   #divide function
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def square_root(x): #square root function
    if x < 0:
        return "Error: Imaginary number!"
    return math.sqrt(x)

def sine(x):    #sin trigono function
    return math.sin(math.radians(x))

def cosine(x):  #cos trigono function
    return math.cos(math.radians(x))

def tangent(x): #tan trigono function
    return math.tan(math.radians(x))

def solve_linear_equations():   #solving two linear eqns
    print("Solving Two Linear Equations of 2 Variables")
    print("-------------------------------------------")
    print("ax + by = c")
    print("dx + ey = f")
    print()

    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    d = float(input("Enter the value of d: "))
    e = float(input("Enter the value of e: "))
    f = float(input("Enter the value of f: "))

    x, y = symbols('x y')
    eq1 = Eq(a*x + b*y, c)
    eq2 = Eq(d*x + e*y, f)
    solution = solve((eq1, eq2), (x, y))

    x_val = solution[x]
    y_val = solution[y]

    print()
    print("Solution:")
    print(f"x = {x_val}")
    print(f"y = {y_val}")

# Main program loop
while True:
    print("Advanced Calculator")
    print("-------------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Sine")
    print("7. Cosine")
    print("8. Tangent")
    print("9. Solve Linear Equations")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ")

    if choice == '10':
        print("Exiting...")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        num = float(input("Enter a number: "))
        print("Result:", square_root(num))
    elif choice == '6':
        angle = float(input("Enter an angle in degrees: "))
        print("Result:", sine(angle))
    elif choice == '7':
        angle = float(input("Enter an angle in degrees: "))
        print("Result:", cosine(angle))
    elif choice == '8':
        angle = float(input("Enter an angle in degrees: "))
        print("Result:", tangent(angle))
    elif choice == '9':
        solve_linear_equations()
    else:
        print("Invalid choice! Please enter a number from 1 to 10.")
    print()
