num = 42339

first_dig = num % 10
sec_dig = (num % 100) // 10
third_dig = (42339 % 1000) // 100
fourth_dig = (42339 % 10000) // 1000
fifth_dig = (42339 // 10000)

print(fifth_dig, "  ", fourth_dig, "  ", third_dig,
      "  ", sec_dig, "  ", first_dig)
