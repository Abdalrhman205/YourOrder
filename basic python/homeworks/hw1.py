# 1 اكتب برنامج لقراءة ثلاثة اعداد ثم اجد حاصل جمعهم وطرحهم وضربهم
# read numbers
a = int(input("Enter first number ="))
b = int(input("Enter seconed number ="))
c = int(input("Enter third number ="))

sum = a + b + c
sub = a - b - c
mul = a * b * c

print("*******   answer question one ******")
# print
print("sum = " + str(sum))
print("sub = " + str(sub))
print("mul = " + str(mul))


print("*******    question two ******")
# 2 اكتب برنامج لقراءة اسمك وعمرك
# read name & age
name = str(input("Enter your name ="))
age = int(input("Enter your age ="))

print("*******   answer question two ******")
print("My name is " + str(name) + " and my age = " + str(age))
