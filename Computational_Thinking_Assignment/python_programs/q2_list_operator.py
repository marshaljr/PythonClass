numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("List:", numbers)
print("Total:", total)
print("Average:", average)
