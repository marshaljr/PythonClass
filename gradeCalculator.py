marks = []
for i in range(5):
    mark = float(input("Enter mark for subject" + str(i + 1) + ":"))
    marks.append(mark)

total = sum(marks)
average = total / 5

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

if all(mark >=50 for mark in marks):
    result = "PASS"
else:
    result = "FAIL"    

print("\n--Result--")    

for i in range(5):
    print("Subject", i+1 , ":" , marks[i])

print("Total Marks:", total)
print("Average Mark:", average)
print("Grade:", grade)
print("Overall Result:", result)    