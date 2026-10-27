numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)

print("The largest number is:", largest)
print("The smallest number is:", smallest)