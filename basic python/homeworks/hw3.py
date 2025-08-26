# 1 اكتب برنامج لقراءة ن  من القيم ثم اوجد اصغر قيمة ؟
# read
n = int(input("Enter n ="))
x = int(input("Enter x ="))
smal =x

for n in range(1,n):
    x = int(input("Enter x ="))
    
    if x<smal:
        smal=x

print("*******   answer question one ******")
print(smal)

# اكتب برنامج لقراءة ن من القيم ثم احد حاصل ضرب القيم الفردية ؟2
print("*******    question two ******")
# read
n = int(input("Enter n ="))
mul =1

for n in range(0,n):
    x = int(input("Enter x =")) 
    if x%2==1:
        mul=mul*x
print("*******   answer question two ******")
print("mul =" + str(mul))

# اكتب برنامج لقراءة ن من القيم ثم قم بطباعة حالة كل عدد هل فردي او زوجي ؟ 3
print("*******    question three ******")

# read
n = int(input("Enter n ="))

print("*******   answer question three ******")
for n in range(0,n):
    x = int(input("Enter x ="))
    if x%2==1:
        
        print(str(x) + " odd فردي")
    else:
        print(str(x) + " even زوجي")


