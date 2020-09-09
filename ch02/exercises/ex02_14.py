# Target Heart-Rate Calculator
age = int(input("Enter your age(years): "))

max_heart_rate = 220 - age
lower_lim = max_heart_rate * 0.5
upper_lim = max_heart_rate * (85 / 100)

print("Your maximum heart rate is: ", max_heart_rate)
print("Your heart rate range: ", lower_lim, "-", upper_lim)
