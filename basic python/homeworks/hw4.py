# اكتب برنامج لقراءة مصفوفة طولها ن ثم قم بطباعةالاعداد الزوجية وحاصل جمعهم والاعداد الفردية وحاصل ضربها ؟ 1
# read
# numbers =[]
# evens_numbers =[]
# odd_numbers =[]
# sum =0
# mul =1
# n = int(input("Enter n ="))

# for i in range(0,n):
#     x = int(input("Enter x ="))
#     numbers.append(x)
#     if x%2==0:
#         sum = sum+x
#         evens_numbers.append(x)
#         print("number " + str(x) + " it's even")
#     else:
#         odd_numbers.append(x)
#         print("number " + str(x) + " it's odd")
#         mul = mul*x

# print("*******   answer question one ******")

# print("sum for evens " + str(sum))
# print("mul for evens " + str(mul))
# print("evens " + str(evens_numbers))
# print("odd " + str(odd_numbers))


print("*******    question two ******")
# اكتب برنامج لقراءة مصفوفة طولها ن ثم اوجد اكبر واصغر قيمة ومكان وجود كلا منهما ؟ 2
# read
numbers =[]
n = int(input("Enter n ="))

for i in range(0,n):
    x = int(input("Enter x ="))
    numbers.append(x)

smal =numbers[0]
# smal_index = 0
big =numbers[0]
# big_index = 0
for i in numbers :
    if  i < smal:
        smal= i
        # smal_index= i
    elif i > big:
        big= i
        # big_index= i

print("*******   answer question two ******")
print("numbers = " + str(numbers))
print("**********************************************")
print("big number = " + str(big))
# print("big_index number = " + str(big_index))
print("**********************************************")
print("smal number = " + str(smal))
# print("smal_index number = " + str(smal_index))

# اكتب برنامج لقراءة مصفوفة طولها ن قم اوجد عدد الاعداد الزوجية؟ 3
print("*******    question three ******")
# read
numbers =[]
even_numbers =[]
n = int(input("Enter n ="))

for i in range(0,n):
    x = int(input("Enter x ="))
    numbers.append(x)

for c in numbers:
    if c%2==0:
        even_numbers.append(c)

print("*******   answer question three ******")
print("len even numbers = " + str(len(even_numbers)))
print("evens Numbers = " + str(even_numbers))
