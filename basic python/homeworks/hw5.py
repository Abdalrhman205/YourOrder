# 1 اكتب برنامج لقراءة مصفوفة طولها ن ثم اوجد اكبر قيمة ؟
arrays = []
n = int(input("Enter number of rows (n): "))
m = int(input("Enter number of columns (m): "))

for i in range(n):
    row = []
    for c in range(m):
        x = int(input("enter x = "))
        row.append(x)
    arrays.append(row)

big = arrays[0][0]

for i in range(n):
    for j in range(m):
        if arrays[i][j] > big:
            big = arrays[i][j]
    
print("*******   answer question one ******")
print("big = " + str(big))
print("arrays = " + str(arrays))

print("*******  question two ******")
# 2 اكتب برنامج لقراءة مصفوفة (أ) طولها ن ثم استخرج القيم الزوجية في مصفوفة جديدية (ب)
arrays = []
even = []

n = int(input("Enter number of rows (n): "))
m = int(input("Enter number of columns (m): "))

for i in range(n):
    row = []
    for c in range(m):
        x = int(input("enter x = "))
        row.append(x)
    arrays.append(row)

for i in range(n):
    for j in range(m):
        if arrays[i][j]%2==0:
            even.append(arrays[i][j])

print("*******   answer question two ******")
print("even = " + str(even))
print("arrays = " + str(arrays))