# 1 اكتب برنامج لقراءة عددين ثم اوجد حاصل جمعهم ثم اوجد هل حاصل فردي او جوزي 
# read
a = int(input("Enter first number ="))
b = int(input("Enter seconed number ="))
# sum
sum = a + b
# print sum  
print("*******   answer question one ******")

print("sum = " +str(sum))
# if even or odd
if sum%2==0 :
    print("even")
else:
    print("odd")
    


# 2 اكتب برنامج اقراءة عددين ثم اوجد اكبر واصغر قيمة وطباعة هل اكبر واصغر قيمة موجب او سالب ؟
print("*******    question two ******")
# read
a = int(input("Enter first number ="))
b = int(input("Enter seconed number ="))
# if a bigger than b 
if a>b:
    max = a
    min = b
elif a==b:
    print("a=b " + str(a) + " = " + str(b))
    max=a
    min=b
    
else: 
    max = b
    min = a

# postive negitive
# max
if max >0 :
    max_pn = str(" postive")
else:
    max_pn= str(" Negtive")
# min
if min >0 :
    min_pn = str(" postive")
else:
    min_pn = str(" Negtive")

print("*******   answer question two ******")
print("max = "  + str(max) + str(max_pn))
print("min = "  + str(min) + str(min_pn))
