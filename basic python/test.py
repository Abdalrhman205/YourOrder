# read numbers
# a = int(input("Enter first number ="))
# b = int(input("Enter seconed number ="))
# c = int(input("Enter third number ="))

# sum = a + b + c
# sub = a - b - c
# mul = a * b * c

# # print
# print("sum = " + str(sum))
# print("sub = " + str(sub))
# print("mul = " + str(mul))


# class Person:
#     name = ""
#     date = ""
#     country = ""
    
# prs1 = Person()
# prs1.name = input("enter name = ")
# prs1.country = input("enter country = ")
# prs1.date = input("enter date = ")  

# print(prs1.name) 
# print(prs1.country) 
# print(prs1.date) 
# # 
# prs = []

# for i in range(3):
#     print(f"\nPerson {i+1}")
#     person = Person()
#     person.name = input("Enter name: ")
#     person.country = input("Enter country: ")
#     person.date = input("Enter date: ")
#     prs.append(person)

# print("\n--- All Persons ---")
# for p in prs:
#     print(f"Name: {p.name}, Country: {p.country}, Date: {p.date}")



# # 2 . Write a Python program to create a calculator class. 
# # Include methods for basic arithmetic operations 

# class Calculator:
#     def calculate(self, a, b, op):
#         if op == "+":
#             return a + b
#         elif op == "-":
#             return a - b
#         elif op == "/":
#             if b == 0:
#                 return "Error: Division by zero"
#             return a / b
#         elif op == "*":
#             return a * b
#         else:
#             return "Invalid operation!"


# calc = Calculator()


# a = float(input("Enter a = "))
# b = float(input("Enter b = "))
# op = input("Enter operation (+, -, *, /): ")


# result = calc.calculate(a, b, op)

# print("Result:", result)

x = int(input("Enter x"))
y = int(input("Enter y"))
for n in range(x+1 ,y):
    if n%2==0:
        print(n)
    