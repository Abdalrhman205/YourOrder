#  1باستخدام الدوال اكتب برنامج لقراءة ن من القيم ثم اوجد حاصل جمعها وقم باستخدام ثلاثة انواع من الدوال ؟
# النوع الاول
print("*******   answer question one 1 ******")
def readNumbers():
    # read 
    n = int(input("Enter n ="))
    sum =0
    for i in range(0,n):
        x = int(input("Enter x ="))
        sum = sum + x
    print("sum = " + str(sum))

readNumbers()

# النوع الثاني
print("*******   answer question one 2 ******")
n = int(input("Enter n ="))
def readNumbers(nnn):
    # read 
    sum =0
    for i in range(0,nnn):
        x = int(input("Enter x ="))
        sum = sum + x
    print("sum = " + str(sum))

readNumbers(n)

# النوع الثالث
print("*******   answer question one 3 ******")
def readNumbers(nnn):
    # read 
    sum =0
    for i in range(0,nnn):
        x = int(input("Enter x ="))
        sum = sum + x
    return "sum = " + str(sum)

n = int(input("Enter n ="))
print(readNumbers(n))


# 2 اكتب برنامج لقراءة عدد ثم طباعة العدد الدي بعده باستخدام انواع الدوال الثلاثة ؟
print("*******  question two ******")
# النوع الاول
print("*******   answer question two 1 ******")
def Number():
    x = int(input("Enter x ="))
    print("number =" , x+1)
Number()

# النوع الثاني
print("*******   answer question two 2 ******")
def Number(x):
    print("number =" , x+1)
x = int(input("Enter x ="))
Number(x)

# النوع الثالث
print("*******   answer question two 3 ******")
def Number(x):
    return  x+1
x = int(input("Enter x ="))
print("number =", Number(x))
