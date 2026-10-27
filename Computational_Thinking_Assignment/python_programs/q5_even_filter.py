numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

if len(numbers) == 0:
    print("No numbers were entered.")
else:
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", even_numbers)