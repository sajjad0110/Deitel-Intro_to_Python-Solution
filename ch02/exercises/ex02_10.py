# Arithmetic, Smallest and Largest

num1 = int(input('Enter an integer: '))
num2 = int(input('Enter another integer: '))
num3 = int(input('Enter another integer: '))

smallest = num1
if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3

largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

print('Sum is:', num1 + num2 + num3)
print('Average:', (num1 + num2 + num3) / 3)
print('Product:', num1 * num2 * num3)
print('Smallest:', smallest)
print('Largest:', largest)
