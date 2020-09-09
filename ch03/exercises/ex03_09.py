# Separating the Digits in an Integer:
# Separating a five-digit integer into its individual
# digits using for loop.
print('Enter five digit integer: ')
num = int(input())
d = 10

if num > 9999 and num < 100000:  # securing the program
    for i in range(5):
        print(((num % d) // (d // 10)))
        d = d * 10
else:
    print('Enter five-digit integer next time. Exiting...')
