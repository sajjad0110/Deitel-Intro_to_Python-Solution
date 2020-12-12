# Nested loops
print('(a)\n')
for i in range(1, 11):
    print('*' * i)

print('\n\n(b)\n')
for i in range(11, 0, -1):
    print('*' * i)

print('\n\n(c)\n')
space = 0
for i in range(11, 0, -1):
    print(' ' * space, '*' * i)
    space = space + 1

print('\n\n(d)\n')
space = 10
for i in range(1, 11):
    print(' '*space, '*'*i)
    space = space - 1
