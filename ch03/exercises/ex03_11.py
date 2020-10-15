# Miles per Gallon
total = 0
counter = 1
gallons = float(input('Enter the gallons used (-1 to end): '))

while gallons != -1:
    miles = float(input('Enter the miles driven: '))
    
    mpg = miles / gallons
    total = total + mpg
    average = total / counter
    counter = counter + 1
    
    print(f'The miles/gallons used for this tank was {mpg:.6f}')
    
    gallons = float(input('Enter the gallons used (-1 to end): '))
    
print(f'The overall average miles/gallon was {average:.6f}')
