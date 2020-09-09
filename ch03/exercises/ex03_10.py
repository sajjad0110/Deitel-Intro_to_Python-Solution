# Seven percent investment return
p = 1000    # original amount invested
r = 7    # annual rate of return
for n in range(1, 30):
    a = p((1 + (r/100)) ** n)
    print('Amount of money each year ' + str(a) + '.')


# This program is uncompleted.
