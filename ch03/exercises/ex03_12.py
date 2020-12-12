# Palindrome
# takes a five-digit number as input from the user and
# show whether it's palindrome or not
number = int(input('Enter five digit number: '))
p = 10000
q = 10
d = 1
flag = 0
if number > 9999 and number < 100000:
    for i in range(2):
        start = (number // p) % 10
        last = (number % q) // d
        if start == last:
            flag = flag + 1
        p = p / 10
        q = q * 10
        d = d * 10
    if flag == 2:
        print(f'{number} is a palindrome.')
    else:
        print('Not palindrome.')
else:
    print('Enter five-digit number. Exiting...')

