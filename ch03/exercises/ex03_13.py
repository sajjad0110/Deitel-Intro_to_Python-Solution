# Factorials
num = int(input('Enter an integer: '))
fact = 1

for i in range(num, 1, -1):
    fact = fact * i

print(fact)
