# Palindrome
# takes a five-digit number as input from the user and
# show whether it's palindrome or not
num = int(input('Enter a five digit integer: '))

if num > 9999 and num < 100000:
    firstDigit = num % 10
    scndDigit = (num % 100) // 10
    thrdDigit = (num % 1000) // 100  # Third digit
    frthDigit = (num % 10000) // 1000    # Fourth Digit
    fifDigit = (num % 100000) // 10000  # Fifth digit

    if firstDigit == fifDigit:
        if scndDigit == frthDigit:
            print(str(num) + ' is a palindrome')
        else:
            print('Not palindrome.')
    else:
        print('Not palindrome')

else:
    print('Enter five-digit number. Exiting...')
