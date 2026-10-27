tuple = ()

for i in range(1, 6):
    num = int(input("Enter a number: "))
    tuple += (num,)

print("First number:", tuple[0])
print("Last number:", tuple[-1])
print("Length of tuple:", len(tuple))
print("Sum of numbers:", sum(tuple))